#coding:utf-8

from django.conf.urls import url, include
import views

urlpantterns = [
    url(r'^login$', views.login)
]