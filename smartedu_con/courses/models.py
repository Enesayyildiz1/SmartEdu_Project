from django.db import models
from django.db.models.base import Model
from teachers.models import Teacher
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,unique=True,null=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,unique=True,null=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    teacher=models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,unique="True",verbose_name="course_name",help_text="enter course name")
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    students=models.ManyToManyField(User,blank=True,related_name='courses_enrolled')
    tags=models.ManyToManyField(Tag,null=True,blank=True)
    desc=models.TextField(max_length=750,blank="true",null="true")
    image=models.ImageField(upload_to="courses/%Y/%m/%d/",default="courses/default_course_image.jpg")
    date=models.DateTimeField(auto_now=True)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create your models here.
