from django.conf.urls import patterns, include, url
from tunes import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^blog/', include('blog.urls')),
)
