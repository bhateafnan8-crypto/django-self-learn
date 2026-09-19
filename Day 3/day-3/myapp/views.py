from django.shortcuts import render
from .models import *
# Create your views here.

def create_user(request):
    User.objects.get_or_create(
        name = "Adfar",
        age=20,
        email="adfar@gmail.com",
        is_paid = False
    )
    User.objects.get_or_create(
        name = "Rasheed",
        age=25,
        email="Rasheed@gmail.com",
        is_paid = True
    )
    User.objects.get_or_create(
        name = "Safdar",
        age=22,
        email="Safdar@gmail.com",
        is_paid = False
    )

    return show_user(request)

def show_user(request):
    users = User.objects.all()

    data = {
        'users':users
    }

    return render(request,'users.html',data)
# def update_user(request):
#     User.objects.get(id=1).update(name="Rasheed")

# def delete_user(request):
#     User.objects.get(id=1).delete()
    
