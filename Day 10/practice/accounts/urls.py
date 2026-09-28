from django.urls import path
from .views import RegisterView,LoginView,LogoutView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='RegisterView'),
    path('login/',LoginView.as_view(),name='LoginView'),
    path('logout/',LogoutView.as_view(),name='LogoutView'),
]