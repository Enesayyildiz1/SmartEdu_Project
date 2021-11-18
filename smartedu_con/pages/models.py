from django.db import models

class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    number=models.CharField(max_length=50)
    message=models.TextField(blank=True)

    def __str__(self):
        return self.email

# Create your models here.
