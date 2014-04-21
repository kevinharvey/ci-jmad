from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from people.views import JmadLoginView
from tunes.views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jmad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^tunes/', include('tunes.urls')),

    # let django-authtool do the accounts/ URLs, with
    # one exception
    url(r'^accounts/login/', JmadLoginView.as_view(), name='login'),
    url(r'^accounts/', include('authtools.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
