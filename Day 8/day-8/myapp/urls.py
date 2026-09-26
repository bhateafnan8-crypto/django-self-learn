from django.urls import path
from myapp.views import prod_list,prod_getpost,pro_getputpatchdlt

urlpatterns = [
    path('api/products/',prod_list,name='prod_list'),
    path('api/prodlist/',prod_getpost,name='prod_getpost'),
    path('api/productdetails/<int:id>/',pro_getputpatchdlt,name='pro_getputpatchdlt'),
]