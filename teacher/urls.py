from django.urls import path
from . import views

urlpatterns = [
    path('myAdmin/Teacher/addTeacher', views.addTeacher, name="addTeacher"),
    path('myAdmin/Teacher/teacherList', views.teacherList,name="teacherList"), 
]