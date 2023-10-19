from django.urls import path
from . import views

urlpatterns = [
    path('addStudent', views.addStudent,name="addStudent"), 
    path('studentList', views.studentList,name="studentList"),
    path('editStudent/<str:id>', views.editStudent,name="editStudent"),
]
