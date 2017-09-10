#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(request.path)
def detail(request, p1, p2, p3):
    return HttpResponse("year:%s,month:%s,day:%s"%(p1, p2, p3))

#展示链接的页面
def getTest1(request):
    return render(request, 'booktest/getTest1.html')

#接受一键一值的情况
def getTest2(request):
    #根据健接收值
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    #构造上下文
    context = {'a':a1, 'b':b1, 'c':c1}
    #向模板中传递上下文
    return render(request, 'booktest/getTest2.html', context)

#接受一键多值的情况
def getTest3(request):
    a1 = request.GET['a']
    a2 = request.GET.getlist('a')
    context = {'a':a1, 'a2':a2}
    return render(request, 'booktest/getTest3.html', context)

def postTest1(request):
    return render(request, 'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname, 'upwd':upwd, 'ugender':ugender, 'uhobby':uhobby}
    return render(request, 'booktest/postTest2.html', context)