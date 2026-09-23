from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def create_user(request):

    if request.method == "POST":

        username = request.POST ["username"]
        password = request.POST ["password"]

        if User.objects.filter(username=username).exists():
            return render(request,'user/user.html',{'error':'User already exists'})
        user = User.objects.create_user(
            username=username,
            password=password
        )
        login(request,user)
        return redirect('show_user')
    return render(request,'user/user.html')

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

            return redirect('show_user')
        else:
            messages.error(request,"Invalid Username or Password")
            return render(request,'login/login.html')

    return render(request,'login/login.html')

def logout_view(request):

    logout(request)

    return redirect('login_view')

@login_required
def show_user(request):
    return render(request,"user/user_list.html")


def home(request):

    if request.user.is_authenticated:
        return render(request,'home/home.html')

    return redirect('login_view')