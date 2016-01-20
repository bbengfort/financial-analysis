# finances.urls
# Application URL definitions and routers.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Tue Jan 19 21:07:35 2016 -0500
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: urls.py [] benjamin@bengfort.com $

"""
Bengfort Finances URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/

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

##########################################################################
## Imports
##########################################################################

from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView


##########################################################################
## URL Patterns
##########################################################################

urlpatterns = [
    # Admin URLs
    url(r'^admin/', admin.site.urls),

    # Application URLs
    url(r'^$', TemplateView.as_view(template_name='site/home.html'), name='home'),

    # Authentication URLs
    # url('', include('social.apps.django_app.urls', namespace='social')),
    url('^accounts/', include('django.contrib.auth.urls')),
]
