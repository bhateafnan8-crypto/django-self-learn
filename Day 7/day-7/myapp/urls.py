from django.urls import path
from myapp.views import product_list,create_products,products_lst,get_product_byID,edit_product,partial_edit_product,dlt_prod
urlpatterns = [
    path('api/products/',product_list,name='product_list'),
    path('api/products_lst/',products_lst,name='products_lst'),
    path('api/create_products/',create_products,name='create_products'),
    path('api/get_product_byID/<int:id>',get_product_byID,name='get_product_byID'),
    path('api/edit_product/<int:id>',edit_product,name='edit_product'),
    path('api/partial_edit_product/<int:id>',partial_edit_product,name='partial_edit_product'),
    path('api/dlt_prod/<int:id>',dlt_prod,name='dlt_prod'),
]
