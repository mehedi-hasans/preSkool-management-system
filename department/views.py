from django.shortcuts import redirect, render

from student.models import courseModel
from django.contrib import messages
# Create your views here.
def addDepartment(request):
    
    error_messages = {
        'success': 'Department Add Successfully',
        'department_exist_error': 'Department already exist',
    }
    if request.method == "POST":
        department_name = request.POST.get("department_name")
        
        print(department_name)
        
        if courseModel.objects.filter(name=department_name):
            messages.error(request, error_messages['department_exist_error'])
        else:
            
            course=courseModel(
                
                name=department_name,
                
            )
            
            course.save()
            messages.success(request, error_messages['success'])
            
            return redirect("departmentList")
       
    
    
    return render(request,"Departments/addDepartment.html")

def departmentList(request):
    
    department = courseModel.objects.all()
    context = {
        "department": department,
    }
    
    return render(request,"Departments/departmentList.html",context)
