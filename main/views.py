from django.shortcuts import render
from .models import ToDoList,Task
from . import forms
from django.http import JsonResponse
from bs4 import BeautifulSoup
import json
from django.contrib.auth.decorators import login_required
from accounts.views import signIn



@login_required
def home(request):
    # Get the New list form
    newListForm = forms.CreateNewList()

    # Get new task form
    newTaskForm = forms.CreateTask()


    #check if user has  todos
    todos_count = len(ToDoList.objects.filter(User=request.user.id))


    #check if user has tasks
    tasks_count = len(Task.objects.all())

    print(tasks_count)

    # Get all todo Lists related to the current user
    todos = ToDoList.objects.filter(User= request.user.id)

    current_list = todos.first()  # Set the default list



    # When the view button is clicked to change the selected todo
    if request.method == "POST" and request.POST.get('action') == "update_view":
        current_listID = request.POST.get("current_listID")
        current_list = ToDoList.objects.get(id=current_listID)
  

        tasks = Task.objects.filter(todolist=current_list)
        context = {
        "todos": todos,
        "newListForm": newListForm,
        "newTaskForm": newTaskForm,
        "selected_list": current_list,
        "tasks":tasks,
        "todos_count":todos_count,
        "tasks_count":tasks_count,
        }

        # Render the entire home view
        rendered_home_view = render(request, "main/home.html",{"context":context})

        # Extract the HTML content of the tasks section
        soup = BeautifulSoup(rendered_home_view.content, 'html.parser')
        tasks_html = str(soup.find('ul', class_='tasks'))



        # Return tasks HTML in JSON response
        return JsonResponse({'tasks_html': tasks_html})

        

    # Get tasks for the selected list
    tasks = Task.objects.filter(todolist=current_list)

    context = {
        "todos": todos,
        "newListForm": newListForm,
        "newTaskForm": newTaskForm,
        "selected_list": current_list,
        "tasks": tasks,
        "todos_count":todos_count,
        "tasks_count":tasks_count,
    }

    return render(request, "main/home.html", {"context": context})




#create new todo list
#request POSTed using ajax
def createNewList(request):
    #check if POST and get data
    if request.POST.get('action') == 'post':
        list_name = request.POST.get('list_name')

        #create an instance to ToDoList with the entered name
        newList = ToDoList(name=list_name)

        #save that instance to database
        newList.save()

        #link that saved todo list with the current user
        request.user.todolist.add(newList)


        #return response as json
        response = JsonResponse({'list name':list_name })
        return response



#delete todo list
def deleteList(request):
    if request.POST.get('action') == "deleteList":
        selected_list_id = request.POST.get('selected_list_id')

        
        #delete the list from database
        selected_list = ToDoList.objects.get(id=selected_list_id)

        selected_list.delete()

        print("deleted")


        response = JsonResponse({"list":selected_list_id})


        return response



#add a task
def addTask(request):
    #check if POST and get data
    if request.POST.get('action') == 'post':
        task = request.POST.get("task_text")
        completed = request.POST.get("completed").capitalize()
        selected_id = request.POST.get("current_listID")

        selected_list = ToDoList.objects.get(id=int(selected_id))

        newTask = Task(text=task,completed=completed)

        newTask.save()

        selected_list.task.add(newTask)


 
  

        tasks = Task.objects.filter(todolist=selected_list)
        context = {
        "tasks":tasks,

        }

        # Render the entire home view
        rendered_home_view = render(request, "main/home.html",{"context":context})

        # Extract the HTML content of the tasks section
        soup = BeautifulSoup(rendered_home_view.content, 'html.parser')
        tasks_html = str(soup.find('ul', class_='tasks'))



        # Return tasks HTML in JSON response
        return JsonResponse({'tasks_html': tasks_html})
        

         




#delete a task
def deleteTask(request):
    # Get all todo Lists related to the current user
    todos = ToDoList.objects.filter(User= request.user.id)

    current_list = todos.first()  # Set the default list


    if request.POST.get("action") == "deleteTask":
        clickedTaskID = request.POST.get("clickedTaskID")
        current_listID = request.POST.get("current_listID")
        current_list = ToDoList.objects.get(id=current_listID)

        #get the clicked task and delete it
        clicked = Task.objects.get(id=clickedTaskID)
        
        #delete it
        clicked.delete()


        tasks = Task.objects.filter(todolist=current_list)
        context = {
        "todos": todos,
        "selected_list": current_list,
        "tasks":tasks,
        }

        # Render the entire home view
        rendered_home_view = render(request, "main/home.html",{"context":context})

        # Extract the HTML content of the tasks section
        soup = BeautifulSoup(rendered_home_view.content, 'html.parser')
        tasks_html = str(soup.find('ul', class_='tasks'))


        #if keep count of tasks to refresh page when all tasks are deleted
        tasks_count = len(Task.objects.all())


        # Return tasks HTML in JSON response
        return JsonResponse({'tasks_html': tasks_html,"count":tasks_count})





#edit a task
def editTask(request):
    if request.POST.get("action") == "editTask":
        clickedTask = request.POST.get("clickedTask")

        response = JsonResponse({"task":clickedTask})

      

    return response





#save changes after editting
def saveChanges(request):
    if request.POST.get("action") == "saveChanges":

        #get ids of the editted tasks from the POST request
        tasks_ids = request.POST.getlist("inputs[]")

        #get current texts of the editted tasks from the POST request
        tasks_texts = request.POST.getlist("texts[]")

        #create a dict,keys are tasks id and value is task text
        editted_tasks = dict(zip(tasks_ids,tasks_texts))

        #get those editted tasks from db to update them
        tasks_to_edit = Task.objects.filter(id__in=tasks_ids) 



        for task_id in tasks_ids:
            for key,val in editted_tasks.items():
                if task_id == key:
                    Task.objects.filter(id=task_id).update(text=val)
                    print("updated")

                    


        response = JsonResponse({'task':editted_tasks})

        return response




#update task completion status
def updateStatus(request):
    if request.POST.get('action') == 'updateStatus':
        checkbox_id = request.POST.getlist('checkbox_id[]')[0] 
        checkbox_status = request.POST.getlist('checkbox_status[]')[0].capitalize() #to get True not true


        #get clicked task's from db and update its completion status
        Task.objects.filter(id=checkbox_id).update(completed=checkbox_status)


        response = JsonResponse({'checkbox':checkbox_id})

        return response