from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import create_user,login_view,logout_view,show_user,home

urlpatterns = [
    path('',login_view,name="login_view"),
    path('createuser/',create_user,name="create_user"),
    path('logout/',logout_view,name="logout_view"),
    path('showuser/',show_user,name="show_user"),
    path('home/',home,name="home"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )