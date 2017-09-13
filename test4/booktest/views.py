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
