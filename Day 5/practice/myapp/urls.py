from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import create_user,create_std,show_std,login_view,logout_view,dashboard,Image_view,Image_show


urlpatterns = [
    path('',create_user,name='create_user'),
    path('createstd/',create_std,name='create_std'),
    path('showstd/',show_std,name='show_std'),
    path('login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view'),
    path('dashboard/',dashboard,name='dashboard'),
    path('imageview/',Image_view,name='image_view'),
    path('imageshow/',Image_show,name='image_show'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )