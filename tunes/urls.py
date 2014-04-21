from django.conf.urls import patterns, include, url
from tunes import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.TunesIndexView.as_view(), name='tunes-index'),
)
