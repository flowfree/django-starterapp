import os
from .base import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
ALLOWED_HOSTS = ['*']

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'postgres',
        'PORT': 5432,
        'NAME': env('POSTGRES_USER'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
    }
}

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_ROOT = '/var/www/static'