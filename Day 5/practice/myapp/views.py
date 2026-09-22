from django.shortcuts import render,redirect
from myapp.forms import UserForm,StudentForm,ImageForm
from myapp.models import Student,Image
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def create_user(request):

    if request.method == "POST":

        form = UserForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

    else:
        form = UserForm()

    return render(request,'user/user.html',{'form':form})

def create_std(request):
    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('show_std')

    else:
        form = StudentForm()

    return render(request,'students/students.html',{'form':form})

def show_std(request):

    std = Student.objects.all()

    data = {
        'std':std
    }

    return render(request,'students/student_list.html',data)

def login_view(request):

    if request.method == "POST":

        username = request.POST ["username"]
        password = request.POST ["password"]

        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        
        else:
            messages.error(request,"Invalid username or password")

    return render(request,'login/login.html')

def logout_view(request):

    logout(request)

    return redirect("login_view")

@login_required
def dashboard(request):
    return render(request,'dashboard/dashboard.html',)

def Image_view(request):

    if request.method == "POST":

        form = ImageForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request,"Profile created successfully")

            return redirect('image_show')

    else:
        form = ImageForm()

    return render(request,'profile/profile.html',{'form':form})

def Image_show(request):
    profs = Image.objects.all()

    return render(request,'profile/profile_list.html',{'profs':profs})