from django.urls import path
from .views import home,reciepe_list,create_reciepe,edit_reciepe,delete_reciepe
urlpatterns = [
    path('',home,name='home'),
    path('reciepe/',reciepe_list,name='reciepe_list'),
    path('create_reciepe/',create_reciepe,name='create_reciepe'),
    path('edit_reciepe/<int:id>',edit_reciepe,name='edit_reciepe'),
    path('delete_reciepe/<int:id>',delete_reciepe,name='delete_reciepe'),
]