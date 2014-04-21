from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tunes.views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jmad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^tunes/', include('tunes.urls')),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
