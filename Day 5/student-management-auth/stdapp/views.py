from django.shortcuts import render,redirect
from stdapp.models import Student
from stdapp.forms import StudentForm
# Create your views here.

def std_create(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("std_show")

    else:
        form = StudentForm()

    return render(request,'students/student_form.html',{'form':form})

def std_show(request):

    std_list = Student.objects.all()

    return render(request,'students/student_list.html',{'std_list':std_list})
