from django.shortcuts import render
from django.http import HttpResponse
from . models import Course,Category,Tag

courses=Course.objects.all()
categories=Category.objects.all()
tags=Tag.objects.all()

def courselist(request):

  
    context={
        'courses':courses,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'courses.html',context)

def course_detail(request,course_id):
    course=Course.objects.get(id=course_id)

    context={
        'course':course
    }
    return render(request, 'course.html',context)

def courses_by_category(request,category_slug):
    courses=Course.objects.all().filter(category__slug=category_slug)

    context={
        'courses':courses,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'courses.html',context)

def courses_by_tags(request,tag_slug):
    courses=Course.objects.all().filter(tags__slug=tag_slug)

    context={
        'courses':courses,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'courses.html',context)

# Create your views here.
