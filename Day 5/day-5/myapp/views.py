from django.shortcuts import render
from myapp.forms import StudentForm
# Create your views here.

def student_create(request):
    form = StudentForm()
    return render(request,'student/studentform.html',{'form':form})
    