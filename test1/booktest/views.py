from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import *

def index(request):
    #return HttpResponse('hello world')
    booklist = BookInfo.objects.all()
    context = {'list':booklist}
    return render(request, 'booktest/index.html', context)

def show(request):


    context = {'list':'herolist'}
    return render(request, 'booktest/show', context)