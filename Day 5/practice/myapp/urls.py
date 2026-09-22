from django.urls import path
from myapp.views import create_user,create_std,show_std,login_view,logout_view,dashboard


urlpatterns = [
    path('',create_user,name='create_user'),
    path('createstd/',create_std,name='create_std'),
    path('showstd/',show_std,name='show_std'),
    path('login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view'),
    path('dashboard/',dashboard,name='dashboard'),
]