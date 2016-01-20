# finances.wsgi
# WSGI config for finances project.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Tue Jan 19 20:53:12 2016 -0500
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: wsgi.py [] benjamin@bengfort.com $

"""
WSGI config for finances project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

##########################################################################
## Imports
##########################################################################

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

##########################################################################
## WSGI Configuration
##########################################################################

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finances.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
