from django.shortcuts import render
from books.models import Books
# Create your views here.

def show_Books(request):
    books = Books.objects.all()

    return render(request,'books/books_list.html',{'books':books})

def high_price_book(request):
    high_price_book = Books.objects.filter(price__gt = 500)

    return render(request,'books/books_list.html',{'high_price_book':high_price_book})


def Django_title_book(request):
    Django_title_book = Books.objects.filter(title__icontains = "Django")

    return render(request,'books/books_list.html',{'Django_title_book':Django_title_book})

def update_price(request):
    Books.objects.filter(id=1).update(price=1200)

    books = Books.objects.all()

    return render(request,'books/books_list.html',{'books':books})

def delete_book(request):
    Books.objects.filter(id=2).delete()

    books = Books.objects.all()

    return render(request,'books/books_list.html',{'books':books})
