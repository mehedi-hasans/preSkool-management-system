from django.urls import path
from . import views

urlpatterns = [
    path('myAdmin/Student/addStudent', views.addStudent,name="addStudent"), 
    path('myAdmin/Student/studentList', views.studentList,name="studentList"),
]
