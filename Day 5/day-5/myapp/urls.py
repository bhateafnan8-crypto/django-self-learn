from django.urls import path
from myapp.views import student_create,user_create,customer_bill_create,invoice_create,job_create

urlpatterns = [
    path('',student_create,name='student_create'),
    path('createuser/',user_create,name='user_create'),
    path('createcustomerbill/',customer_bill_create,name='customer_bill_create'),
    path('createinvoice/',invoice_create,name='invoice_create'),
    path('createjob/',job_create,name='job_create'),
]