"""
URL configuration for stdproject project.

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
from django.urls import path
from stdapp.views import add_stud,show_stud,update_stud,delete_stud

urlpatterns = [
    path('',show_stud,name='show_stud'),
    path('create/',add_stud,name='add_stud'),
    path('update/',update_stud,name='update_stud'),
    path('delete/',delete_stud,name='delete_stud'),

]
