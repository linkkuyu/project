from django.conf.urls import url
import views

urlpatterns = {
    url(r'^$', views.index),
    url(r'^uploadPic$', views.uploadPic),
    url(r'^uploadHandle$', views.uploadHandle),

}