from django.shortcuts import render
from .models import Book
from django.http import HttpRequest, HttpResponseRedirect

# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def book(request):
    books = Book.objects.all()
    return render(request, 'viewbook.html', {"books":books})

def add_book(request):
    return render(request, 'addbook.html')

def addBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        book=Book()
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')

