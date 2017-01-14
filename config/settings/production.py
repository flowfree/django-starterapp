import os
from .base import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['example.com']) 

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# ------------------------------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY')

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# ------------------------------------------------------------------------------
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

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = "anymail.backends.sendgrid.SendGridBackend"
ANYMAIL = {
    "SENDGRID_USERNAME": env('SENDGRID_USERNAME'),
    "SENDGRID_PASSWORD": env('SENDGRID_PASSWORD'),
}

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_ROOT = '/var/www/static'

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
MEDIA_ROOT = '/var/www/media'

# CELERY CONFIGURATION
# ------------------------------------------------------------------------------
BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
