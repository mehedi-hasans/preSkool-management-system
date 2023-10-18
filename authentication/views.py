from django.shortcuts import redirect, render

# Create your views here.
def signupPage(request):
    return render(request, "signup.html")

def loginPage(request):
    return render(request, "login.html")