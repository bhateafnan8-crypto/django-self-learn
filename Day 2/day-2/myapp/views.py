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

def person(request):
    users = [{
        "name":"Adfar",
        "age":20
    },
    {
        "name":"Rasheed",
        "age":19
    },
    {
        "name":"Shahid",
        "age":16
    },
    {
        "name":"Amaan",
        "age":15
    }
    ]

    return render(request,'person.html',{"users":users})

def products(request):
    products_list = ["Mobile","Laptop","Charger","Keyboard","Tv"]

    return render(request,'products.html',{"products":products_list})

def home1(request):
    return render(request,'home1.html')
def about1(request):
    return render(request,'about1.html')
def Context1(request):
    return render(request,'Context1.html') 
def products1(request):
    return render(request,'products1.html')
def porfolio1(request):
    return render(request,'porfolio1.html')

def index(request):
    return render(request,'index.html')