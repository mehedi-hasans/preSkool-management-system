from django.urls import path
from . import views

urlpatterns = [
    path('addStudent', views.addStudent,name="addStudent"),
]
