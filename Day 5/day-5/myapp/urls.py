from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import student_create,user_create,customer_bill_create,invoice_create,job_create,login_view,logout_view,dashboard,check_curr_user,session,visited

urlpatterns = [
    path('',student_create,name='student_create'),
    path('createuser/',user_create,name='user_create'),
    path('createcustomerbill/',customer_bill_create,name='customer_bill_create'),
    path('createinvoice/',invoice_create,name='invoice_create'),
    path('createjob/',job_create,name='job_create'),
    path('login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view'),
    path('dashboard/',dashboard,name='dashboard'),
    path('user/',check_curr_user,name='check_curr_user'),
    path('session/',session,name='session'),
    path('visited/',visited,name='visited'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )