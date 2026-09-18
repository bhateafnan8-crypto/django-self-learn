from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    context = {
        "projects": [
            "Python Calculator",
            "Django Portfolio",
            "Todo Application",
        ]
    }

    return render(request, "project.html", context)

def contact(request):
    return render(request, "contact.html")