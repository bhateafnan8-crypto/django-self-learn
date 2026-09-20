from django.shortcuts import render,redirect
from myapp.models import Student,students

# Create your views here.

def create_stud(request):
    Student.objects.get_or_create(
        name = 'Safdar',
        age = 25
    )
    Student.objects.get_or_create(
        name = 'Haider',
        age = 22
    )

    students.objects.get_or_create(
        name='Sadik',
        email='Sadik@ex.com',
        is_pass= False,
        gr_num = 12783

    )

    students.objects.get_or_create(
        name='Huzaif',
        email='Huzaif@ex.com',
        is_pass= False,
        gr_num = 12722

    )
    students.objects.get_or_create(
        name='Sakib',
        email='Sakib@ex.com',
        is_pass= False,
        gr_num = 12753

    )

    return redirect('show_stud')    

def show_stud(request):
    students_list = Student.objects.all()
    students_list_1 = students.objects.all()

    return render(request,'myapp.html',{"students_list":students_list,'students_list_1':students_list_1})

def update_stud_age(request):
    Student.objects.filter(id=2).update(age=19)
    students.objects.filter(id=2).update(is_pass=True)

    students_list = Student.objects.all()
    students_list_1 = students.objects.all()

    return render(request,'myapp.html',{"students_list":students_list,'students_list_1':students_list_1})


def delete_stud(request):
    Student.objects.filter(id=3).delete()
    students.objects.filter(id=3).delete()
    
    students_list = Student.objects.all()
    students_list_1 = students.objects.all()

    return render(request,'myapp.html',{"students_list":students_list,'students_list_1':students_list_1})

