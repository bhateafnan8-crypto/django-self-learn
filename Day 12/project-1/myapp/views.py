from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,aauthenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomRegisterForm

# Create your views here.


def registered_view(request):

    if request.method == "POST":
        form =  CustomRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success('request','Account successfully created, please login.')
            return redirect('login')
    else:
        form = CustomRegisterForm()
        return render('request','registeration/register.html',{'form':form})

