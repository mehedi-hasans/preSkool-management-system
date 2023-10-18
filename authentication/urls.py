from django.urls import path
from . import views
urlpatterns = [
    path('', views.signupPage,name="signupPage"), 
    path('loginPage', views.loginPage,name="loginPage"), 
 
]