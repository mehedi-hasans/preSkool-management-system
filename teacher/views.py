from django.shortcuts import redirect, render

from authentication.models import customUser
from django.contrib import messages
from student.models import courseModel
from teacher.models import teacherModel

# Create your views here.
def addTeacher(request):
    error_messages = {
        'success': 'Teacher Add Successfully',
        'erroremail': 'email already exist',
        'errorusername': 'username already exist',
    }
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")  # Changed from 'user_name' to 'username'
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        course_id = request.POST.get("courseid")
        mobile = request.POST.get("mobile")
        experience = request.POST.get("experience")

        # Check if email or username already exists
        if customUser.objects.filter(email=email).exists():
            messages.error(request, error_messages['erroremail'])
        if customUser.objects.filter(username=username).exists():
            messages.error(request, error_messages['errorusername'])
        else:
            # Create the customUser instance
            user = customUser.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.profile_pic = profile_pic
            user.user_type = 2  # Assuming '2' represents students

            # Save the user instance
            user.save()

            # Retrieve the selected course and session year
            myCourse = courseModel.objects.get(id=course_id)

            # Create the student instance
            teacher = teacherModel(
                admin=user,
                address=address,
                courseid=myCourse,
                gender=gender,
                mobile=mobile,
                experience=experience,
            )

            # Save the student instance
            teacher.save()

            messages.success(request, error_messages['success'])
            return redirect("teacherList")

    # Fetch the course and session year data to display in the form
    course = courseModel.objects.all()
    st=teacherModel.objects.all()
    context = {
        "course": course,
    }

    return render(request, "Teachers/addTeacher.html", context)



def teacherList(request):
    
    allTeacher=teacherModel.objects.all()
    print(allTeacher)
    
    return render(request,"Teachers/teacherList.html",{"teacher":allTeacher})


