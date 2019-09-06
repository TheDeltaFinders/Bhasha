#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : buried
# update : 2019-09-06 16:47

from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path(r'', views.KoshIndex.as_view(), name='index'),
    re_path('meaning/(?P<pslug>[^\x00-\x7F]*[/~]*[^\x00-\x7F]*)$', views.WordMeaning.as_view(), name='meaning'),
    #path('meaning/<str:pslug>', views.WordMeaning.as_view(), name='meaning'),
    #url(r'^download$',views.BlogDownload.as_view(), name="download"),
]

handler404 = 'kosh.views.handler404'
