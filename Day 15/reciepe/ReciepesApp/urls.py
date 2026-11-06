from django.urls import path
from .views import home,reciepe
urlpatterns = [
    path('',home,name='home'),
    path('reciepe/',reciepe,name='reciepe'),
]