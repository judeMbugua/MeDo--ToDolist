from django.db import models
from django.contrib.auth.models import User

#the toDolist model
class ToDoList(models.Model):
	#every created todoList must be related to a user,,setting null to true to avoid integrity error
	User = models.ForeignKey(User,on_delete=models.CASCADE,related_name='todolist', null=True)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name




class Task(models.Model):
	todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE,related_name="task", null=True)
	text = models.CharField(max_length=200)
	completed = models.BooleanField()
