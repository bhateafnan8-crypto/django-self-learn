from django.urls import path
from myapp.views import ProfileView,AdminView,ProductsView
urlpatterns = [
    path('api/profile/',ProfileView.as_view(),name='ProfileView'),
    path('api/admin/',AdminView.as_view(),name='AdminView'),
    path('api/products/',ProductsView.as_view(),name='ProductsView'),
]