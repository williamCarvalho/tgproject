from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.consulta, name='consulta'),
    url(r'^resultado/$', views.resultado, name='resultado'),
    url(r'^lista/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^charts/chart.png$', views.simple, name='chart'),
]