# -*- coding: utf-8 -*-
from django.conf.urls import url, include

__author__ = 'erhmutlu'

urlpatterns = [
    url(r'^', include('poogleauth.urls')),
]
