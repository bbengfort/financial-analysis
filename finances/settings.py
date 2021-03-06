# finances.settings
# The common Django settings for the Finance Analysis project.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Tue Jan 19 20:43:16 2016 -0500
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: settings.py [] benjamin@bengfort.com $

"""
Django settings for finances project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

##########################################################################
## Imports
##########################################################################

import os
import dj_database_url


##########################################################################
## Helper function for environmental settings
##########################################################################

def environ_setting(name, default=None):
    """
    Fetch setting from the environment- if not found, then this setting is
    ImproperlyConfigured.
    """
    if name not in os.environ and default is None:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(
            "The {0} ENVVAR is not set.".format(name)
        )

    return os.environ.get(name, default)

##########################################################################
## Build Paths inside of project with os.path.join
##########################################################################

PROJECT = os.path.dirname(os.path.abspath(__file__))
REPOSITORY = os.path.dirname(PROJECT)


##########################################################################
## Database Settings
##########################################################################

## Database
## https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(),
}

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

##########################################################################
## Secret settings - do not store!
##########################################################################

## SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ_setting("SECRET_KEY")

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

##########################################################################
## Runtime settings
##########################################################################

## Debugging settings
## SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

## Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

## Hosts
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS  = ('127.0.0.1', '198.168.1.10')

## WSGI Configuration
ROOT_URLCONF = 'finances.urls'
WSGI_APPLICATION = 'finances.wsgi.application'

## Application definition
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'django_gravatar',
]

## Request Handling
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

## Internationalization
## https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'America/New_York'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

##########################################################################
## Content (Static, Media, Templates)
##########################################################################

## Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

## Static files (CSS, JavaScript, Images)
## https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/assets/'


STATICFILES_DIRS = (
    os.path.join(PROJECT, 'assets'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

## Content
MEDIA_ROOT       = os.path.join(PROJECT, 'media')
STATIC_ROOT      = 'staticfiles'

##########################################################################
## Logging and Error Reporting
##########################################################################

ADMINS          = (
    ('Benjamin Bengfort', 'benjamin@bengfort.com'),
)

SERVER_EMAIL    = 'Dakota Server <server@bengfort.com>'
EMAIL_USE_TLS   = True
EMAIL_HOST      = 'smtp.gmail.com'
EMAIL_HOST_USER      = environ_setting("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD  = environ_setting("EMAIL_HOST_PASSWORD")
EMAIL_PORT      = 587
EMAIL_SUBJECT_PREFIX = '[FINANCES] '
