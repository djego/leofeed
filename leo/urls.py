from django.conf.urls import patterns, url

from leo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)