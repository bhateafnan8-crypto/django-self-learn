"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import show_Books
from books.views import high_price_book
from books.views import Django_title_book
from books.views import update_price
from books.views import delete_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',show_Books,name='show_Books'),
    path('highprice/',high_price_book,name='high_price_book'),
    path('DjangoBook/',Django_title_book,name='Django_title_book'),
    path('updateprice/',update_price,name='update_price'),
    path('deletebook/',delete_book,name='delete_book'),
]
