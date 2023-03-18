from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello_world_view(request):
    return HttpResponse("<h1> Hello world! This is my first DJANGO project </h1>")
# Create your views here.


def book_view(request):
    book = models.Book.objects.all()
    return render(request, 'index.html', {'book': book})
# Create your views here.
