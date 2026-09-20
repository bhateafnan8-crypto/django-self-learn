from django.shortcuts import render
from myapp.forms import StudentForm,UserForm
# Create your views here.

def student_create(request):
    form = StudentForm()
    return render(request,'student/studentform.html',{'form':form})


def user_create(request):

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = UserForm()

    return render(request, "user/user.html", {"form": form})