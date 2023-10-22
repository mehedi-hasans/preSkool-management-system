from django.urls import path
from . import views

urlpatterns = [
    path('myAdmin/Student/addStudent', views.addStudent,name="addStudent"), 
    path('myAdmin/Student/studentList', views.studentList,name="studentList"), 
    path('myAdmin/Student/editStudent/<str:id>', views.editStudent,name="editStudent"), 
    path('myAdmin/Student/updateStudent', views.updateStudent,name="updateStudent"),
    path('studentDelete/<str:id>',views.studentDelete,name="studentDelete"),
]
