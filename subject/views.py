from django.shortcuts import render, redirect
from django.contrib import messages

from student.models import courseModel
from subject.models import subjectModel
from teacher.models import teacherModel

# Create your views here.
def addSubject(request):
    
    course=courseModel.objects.all()
    teacher=teacherModel.objects.all()
    
    
    error_messages = {
        'success': 'Subject Add Successfully',
        'subjecterror': 'Subject already exist',
    }
    if request.method == "POST":
        course_id = request.POST.get("course_id")
        teacher_id = request.POST.get("teacher_id")
        subject_name = request.POST.get("subject_name")
       
        courseid=courseModel.objects.get(id=course_id)
        teacherid=teacherModel.objects.get(id=teacher_id)
    
        subject=subjectModel(
        name=subject_name,
        course=courseid,
        teacher=teacherid,
        )
        
        subject.save()
        messages.success(request, error_messages['success'])

        return redirect("subjectList")
    
    context={
        "course":course,
        "teacher":teacher,
        }    

    return render(request,"Subjects/addSubject.html", context)


def subjectList(request):
    
    subject = subjectModel.objects.all()
    context = {
        "subject": subject,
    }
    
   
    return render(request,"Subjects/subjectList.html", context)
