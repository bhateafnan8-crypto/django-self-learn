from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class students(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gr_num = models.IntegerField()
    is_pass = models.BooleanField(default=False)

    def __str__(self):
        return self.name