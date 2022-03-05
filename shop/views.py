from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

#def index(request):
# return render(request, "index.html")

def list(request):
    Data = {'Books': Book.objects.all().order_by("-id")[:3]}
    return render(request, 'index.html', Data)

def showBook(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'book.html', {'book': book})