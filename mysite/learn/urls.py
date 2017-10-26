from django.conf.urls import include, url
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='home'),
    url(r'^add/$', views.add, name="add"),
    # url(r'^add/(\d+)/(\d+)/$', views.add2, name="add2"),
    url(r'^add/(\d+)/(\d+)/$', views.add2),
    url(r'^add_new/(\d+)/(\d+)/$', views.add3, name="add3"),
]
