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
    
def editBookView(request):
        book = Book.objects.get(id=request.GET['bookid'])
        print(book)
        return render(request, 'editbook.html', {"book":book})

def editBook(request):
     if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        book=Book.objects.get(id=request.POST['bookid'])
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')
     

def deleteBook(request):
      book=Book.objects.get(id=request.POST['bookid'])
      book.delete()
      return HttpResponseRedirect("/")