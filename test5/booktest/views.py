from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
    return render(request,'booktest/index.html')

def uploadPic(request):
    return render(request, 'booktest/uploadPic.html')

def uploadHandle(request):
    pic1 = request.FILES['pic1']
    picname = os.path.join(settings.MEDIA_ROOT, pic1.name)
    with open(picname, 'w') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse(picname)




