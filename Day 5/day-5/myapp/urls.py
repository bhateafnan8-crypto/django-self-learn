from django.urls import path
from myapp.views import student_create

urlpatterns = [
    path('',student_create,name='student_create')
]