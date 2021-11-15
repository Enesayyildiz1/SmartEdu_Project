from django.shortcuts import render
from django.http import HttpResponse
from . models import Course

def courselist(request):

    courses=Course.objects.all()

    context={
        'courses':courses
    }
    return render(request, 'courses.html',context)

def course_detail(request,course_id):
    course=Course.objects.get(id=course_id)

    context={
        'course':course
    }
    return render(request, 'course.html',context)

# Create your views here.
