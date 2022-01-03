from boolean_switch.views import switch
from django import get_version
from distutils.version import StrictVersion
from django.urls import include, re_path

from django.contrib import admin
admin.autodiscover()


if StrictVersion(get_version()) > StrictVersion('1.8'):
    urlpatterns = [
        re_path(r'^(?P<url>.*)/switch/$', switch, name='switch'),
    ]
else:
    from django.conf.urls import patterns

    urlpatterns = patterns('',
                           re_path(r'^(?P<url>.*)/switch/$',
                                   switch, name='switch'),
                           )
