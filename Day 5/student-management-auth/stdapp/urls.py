from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from stdapp.views import login_view,logout_view,std_dashboard,std_form_create,std_show,std_update,std_delete,register_view

urlpatterns = [
    path('',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('stddashboard/',std_dashboard,name="dashboard"),
    path('createstudent/',std_form_create,name="studentform"),
    path('showstudent/',std_show,name="stdshow"),
    path('update/<int:pk>/', std_update, name="stdupdate"),
    path('delete/<int:pk>/', std_delete, name="stddelete"),
    path('register/', register_view, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )