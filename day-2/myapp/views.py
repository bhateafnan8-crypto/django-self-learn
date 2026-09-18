from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html') # templates/

def about(request):
    return render(request,'about.html') # templates/

def data(request):
    data = {
        "name":"Adfar",
        "age":20
    } 

    return render(request,'data.html',data)

def context(request):
    context = {
        "company":"Google",
        "Position":"Ai Developer",
        "Vancancies":20
    }

    return render(request,'context.html',context)

def portfolio(request):
    context = {
        "name":"Adfar Shaikh",
        "age":20,
        "company":"Gemini",
        "salary":10000
    }

    return render(request,'portfolio.html',context)