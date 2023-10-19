from django.urls import path
from . import views

urlpatterns = [
    path('myAdmin/Student/addStudent', views.addStudent,name="addStudent"),
]
