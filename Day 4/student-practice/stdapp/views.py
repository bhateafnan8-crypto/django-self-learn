from django.shortcuts import render,redirect
from stdapp.models import Student
# Create your views here.

def add_stud(request):
    Student.objects.get_or_create(
        name = 'Rahul',
        age = 21,
        email = 'rahul@example.com',
        course = 'Django'
    )
    Student.objects.get_or_create(
        name = 'Priya',
        age = 22,
        email = 'priya@example.com',
        course = 'Python'
    )

    return redirect('show_stud')

def show_stud(request):
    students = Student.objects.all()

    django_std = Student.objects.filter(course='Django')

    return render(request,'students/student_list.html',{'students':students,'django_std':django_std})

def update_stud(request):
    Student.objects.filter(course='React').update(course='Java')

    students = Student.objects.all()

    return render(request,'students/student_list.html',{'students':students})

def delete_stud(request):
    Student.objects.filter(name='Priya').delete()

    students = Student.objects.all()

    return render(request,'students/student_list.html',{'students':students})