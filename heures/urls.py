from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^adminPersonne/$', views.adminPersonne, name='adminPersonne'),
    url(r'^adminPersonne/nouvellePersonne/$', views.nouvellePersonne, name='nouvellePersonne'),
    url(r'^adminPersonne/deletePersonne/(?P<pk>\d+)/$', views.deletePersonne.as_view(), name='deletePersonne'),
    
]