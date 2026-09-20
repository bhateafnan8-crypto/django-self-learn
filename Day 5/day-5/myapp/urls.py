from django.urls import path
from myapp.views import student_create,user_create

urlpatterns = [
    path('',student_create,name='student_create'),
    path('createuser/',user_create,name='user_create'),
]