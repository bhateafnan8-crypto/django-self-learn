from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def reciepe(request):
    return render(request,'reciepe_list.html')