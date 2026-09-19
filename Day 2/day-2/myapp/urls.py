"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp.views import home
from myapp.views import about
from myapp.views import data    
from myapp.views import context    
from myapp.views import portfolio
from myapp.views import person
from myapp.views import products
from myapp.views import home1
from myapp.views import about1
from myapp.views import porfolio1
from myapp.views import Context1
from myapp.views import products1
from myapp.views import index
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('about/',about),
    path('data/',data),
    path('context/',context),
    path('portfolio/',portfolio),
    path('person/',person),
    path('products/',products),
    path('home1/',home1),
    path('about1/',about1),
    path('products1/',products1),
    path('Context1/',Context1),
    path('porfolio1/',porfolio1),
    path('index/',index),
]