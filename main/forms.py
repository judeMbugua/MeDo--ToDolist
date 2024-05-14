from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="ToDo List Name",max_length=100)
   

class CreateTask(forms.Form):
    text = forms.CharField(label="Task",max_length=200)
    completed = forms.BooleanField()