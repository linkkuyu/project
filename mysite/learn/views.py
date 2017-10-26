#coding:utf-8

from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(resquest):
    # return HttpResponse(u"欢迎光临")
    return render(resquest, 'home.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    return HttpResponseRedirect(
        reverse('add3', args=(a, b))
    )

def add3(request, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))
