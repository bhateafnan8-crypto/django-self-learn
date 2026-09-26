from django.urls import path
from myapp.views import ProfileView,ProfilesView,HomeView,AdminView,users,DashboardView

urlpatterns = [
    path('api/profile/',ProfileView.as_view(),name='ProfileView'),
    path('api/profiles/',ProfilesView.as_view(),name='ProfilesView'),
    path('api/home/',HomeView.as_view(),name='HomeView'),
    path('api/admin/',AdminView.as_view(),name='AdminView'),
    path('api/users/',users,name='users'),
    path('api/dashboard/',DashboardView.as_view(),name='DashboardView'),
]
