from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from courses.models import Course
import logging
logger = logging.getLogger(__name__)
def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    messages.info(request,'Disable Account')
            else:
                messages.info(request,'Check your username and password')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})



def user_register(request):
    if request.method=="POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'User have created successfully. You can login now')
            return redirect('login')
        else:
           pass
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})            
                

@login_required
def user_dashboard(request):
    current_user=request.user
    courses=current_user.courses_enrolled.all()
    context={
        'courses':courses
    } 

    return render(request,'dashboard.html',context) 

def user_logout(request):
    logout(request)
    return redirect('index')

def enroll_the_course(request):
   course_id=request.POST['course_id']
   user_id=request.POST['user_id']
   course=Course.objects.get(id=course_id)
   user=User.objects.get(id=user_id)
   course.students.add(user)
   return redirect("dashboard")

def release_the_course(request):
   course=Course.objects.get(id=request.POST['course_id'])
   user=User.objects.get(id=request.POST['user_id'])
   course.students.remove(user)
   return redirect("dashboard")

# Create your views here.
