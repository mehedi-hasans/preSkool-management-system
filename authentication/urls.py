from django.urls import path
from . import views
urlpatterns = [
    path('', views.signupPage,name="signupPage"), 
    path('loginPage', views.loginPage,name="loginPage"), 
    path('myAdmin/home', views.adminPage,name="adminPage"),
    path('myProfile/', views.myProfile,name="myProfile"),
    path('profile/profileUpdate', views.profileUpdate,name="profileUpdate"),
 
]