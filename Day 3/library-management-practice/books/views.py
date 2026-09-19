from django.shortcuts import render
from books.models import Books
# Create your views here.

def show_Books(request):
    books = Books.objects.all()

    return render(request,'books/books_list.html',{'books':books})

def high_price_book(request):
    high_price_book = Books.objects.filter(price_gt = 500)

def Django_title_book(request):
    Django_title_book = Books.objects.filter(title_contains = "Django")
