from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . models import Course,Category,Tag
import logging
from django.contrib.auth.models import User


categories=Category.objects.all()
tags=Tag.objects.all()


def courselist(request,category_slug=None,tag_slug=None):
    category_page=None
    tag_page=None
  
    current_user=request.user
    if category_slug != None:
        category_page=get_object_or_404(Category, slug=category_slug)
        courses=Course.objects.all().filter(available=True,category=category_page)

    elif tag_slug != None:
        tag_page =get_object_or_404(Tag,slug=tag_slug)
        courses=Course.objects.all().filter(available=True,tags=tag_page)

    else:
        courses=Course.objects.all()
        
        if(current_user.is_authenticated):
            courses=Course.objects.all()
            enrolled_course=current_user.courses_enrolled.all()
            for course in enrolled_course:
                logging.warning(course)
                courses=courses.exclude(id__in=[course.id])
        
           
        logging.warning(courses)
        



    context={
        'courses':courses,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'courses.html',context)    
    






def course_detail(request,course_id):
    current_user=request.user
    course=Course.objects.get(id=course_id)
    courses=Course.objects.all()
    if current_user.is_authenticated:
        enrolled_courses=current_user.courses_enrolled.all()
    else:
        enrolled_courses=courses
    logging.warning(course.teacher)
    context={
        'course':course,
        'enrolled_courses':enrolled_courses
    }
    return render(request, 'course.html',context)


def search(request):
    courses=Course.objects.filter(name__contains =request.GET['search'])
    context={
        'courses':courses,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'courses.html',context)    
    
# Create your views here.

"""def courselist(request):

  
    context={
        'courses':courses,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'courses.html',context)"""
"""def courses_by_category(request,category_slug):
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
    return render(request, 'courses.html',context)"""