from django.urls import path
from . import views

urlpatterns = [
    path('myAdmin/department/adddepartment', views.addDepartment, name="addDepartment"),
    path('myAdmin/department/departmentlist', views.departmentList,name="departmentList"), 
]