from django.urls import path
from myapp.views import products,prod_lst
urlpatterns = [
    path('api/products/',products,name='products'),
    path('api/products/<int:id>/',prod_lst,name='prod_lst'),

]