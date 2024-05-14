from . import views
from django.urls import path

urlpatterns = [
    path("", views.home,name='home'),
    path("createNewList/", views.createNewList,name='createNewList'),
    path("addTask/", views.addTask,name='addTask'),
    path("deleteTask/", views.deleteTask,name='deleteTask'),
    path("editTask/", views.editTask,name='editTask'),
    path("saveChanges/", views.saveChanges,name='saveChanges'),
    path('updateStatus/',views.updateStatus,name="updateStatus"),
    path('deleteList/',views.deleteList,name="deleteList")


]