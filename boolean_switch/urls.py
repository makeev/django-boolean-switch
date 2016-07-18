from django import get_version
from distutils.version import StrictVersion
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from boolean_switch.views import switch

if StrictVersion(get_version()) > StrictVersion('1.8'):
    urlpatterns = [
        url(r'^(?P<url>.*)/switch/$', switch, name='switch'),
    ]
else:
    urlpatterns = patterns('',
        url(r'^(?P<url>.*)/switch/$', switch, name='switch'),
    )
