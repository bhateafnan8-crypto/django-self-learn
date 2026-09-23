from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import create_user,show_user,home,MyLoginView,MyLogoutView
# from myapp.views import create_user,login_view,logout_view,show_user,home,MyLoginView,MyLogoutView
from django.contrib.auth import views 
# from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('',login_view,name="login_view"),
    path('createuser/',create_user,name="create_user"),
    # path('logout/',logout_view,name="logout_view"),
    path('showuser/',show_user,name="show_user"),
    path('home/',home,name="home"),
    path('', MyLoginView.as_view(),name="login_view"),
    path('logout/', MyLogoutView.as_view(),name="logout_view"),
    # path('', auth_views.login_view.as_view(), name='login_view'),
    # path('logouts/', auth_views.LogoutView.as_view(), name='logout_view'),
    # path('', auth_views.LoginView.as_view(template_name = 'login/login.html'), name='login_view'),
    # path('logins/', auth_views.LoginView.as_view(template_name = 'login/login.html'), name='login_view'),
    # path('logouts/', auth_views.LogoutView.as_view(next_page='login_view'), name='logout_view'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )