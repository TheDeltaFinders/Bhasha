#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# update : 2019-09-06 16:38 

"""bhasha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#Adding the following two lines
#from django.conf import settings
#from django.conf.urls.static import static

import django.views.defaults

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('kosh.urls','kosh'), namespace='kosh')),
    path('kosh/',include(('kosh.urls','kosh'), namespace='kosh')),
] # + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


