from django import get_version
from distutils.version import StrictVersion
from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from boolean_switch.views import switch

if StrictVersion(get_version()) > StrictVersion('1.8'):
    urlpatterns = [
        url(r'^(?P<url>.*)/switch/$', switch, name='switch'),
    ]
else:
	from django.conf.urls import patterns

    urlpatterns = patterns('',
        url(r'^(?P<url>.*)/switch/$', switch, name='switch'),
    )
