from django.db import models
from django.db.models.base import Model

class Course(models.Model):
    name=models.CharField(max_length=200,unique="True")
    desc=models.TextField(max_length=750,blank="true",null="true")
    image=models.ImageField(upload_to="courses/%Y/%m/%d/",default="courses/default_course_image.jpg")
    date=models.DateTimeField(auto_now=True)
    available=models.BooleanField(default=True)

# Create your models here.
