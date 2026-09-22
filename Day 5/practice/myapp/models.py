from django.db import models

# Create your models here.

class Student(models.Model):

    COURSE_CHOICES = [
        ('DS','DataScience'),
        ('IT','InformationTechnology'),
        ('CS','CompuerScience'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age =  models.IntegerField()
    course = models.CharField(max_length=2,choices=COURSE_CHOICES,blank=True)


    def __str__(self):
        return self.name