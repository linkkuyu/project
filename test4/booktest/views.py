#coding:utf-8
from django.shortcuts import render
from models import *

def index(request):
    # hero = HeroInfo.objects.get(pk=1)
    # context = {'hero':hero}
    list = HeroInfo.objects.filter(isDelet=False)
    context = {'list':list}
    return render(request, 'booktest/index.html', context)

def show(request, id, id2):
    context = {'id':id}
    return render(request,'booktest/show.html', context)

#练习模板的继承
def index2(request):
    return render(request, 'booktest/index2.html')

def user1(request):
    context = {'uanme':'习总'}
    return render(request, 'booktest/user1.html', context)

def user2(request):
    return render(request, 'booktest/user2.html')

#html转义

def htmlTest(request):
    context = {'t1':'<h1>123<h1>'}
    return render(request, 'booktest/htmlTest.html', context)

#csrf
def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    context = {'uname':uname}
    return render(request, 'booktest/csrf2.html', context)
