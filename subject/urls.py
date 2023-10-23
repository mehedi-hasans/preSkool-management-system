from django.urls import path
from . import views

urlpatterns = [
    path('myAdmin/subject/addsubject', views.addSubject, name="addSubject"),
    path('myAdmin/subject/subjectlist', views.subjectList,name="subjectList"), 
]