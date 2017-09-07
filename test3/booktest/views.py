#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello word')
def detail(request, p1, p2, p3):
    return HttpResponse("year:%s,month:%s,day:%s"%(p1, p2, p3))