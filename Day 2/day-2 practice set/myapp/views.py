from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to Django")

def username(request):
    user = {
        "name":"Rahul",
        "age":20
    }

    return render(request,'username.html',user)

def validation(request):
    context = [
        {
            "name":"Adfar",
            "age":16
        },
        {
            "name":"Sadik",
            "age":18
        },
        {
            "name":"Shahid",
            "age":20
        },
        {
            "name":"Rasheed",
            "age":22
        },
    ]

    return render(request,'validation.html',{"context":context})

def products(request):
    products = ["Mobile","Tv","Computer","Laptop"]

    return render(request,'product.html',{"products":products})


def portfolio(request):
    return render(request,'portfolio.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def homes(request):
    return render(request,'homes.html')

def abouts(request):
    return render(request,'abouts.html')

def contacts(request):
    return render(request,'contacts.html')