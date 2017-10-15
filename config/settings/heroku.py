import os
import dj_database_url
from .base import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
ALLOWED_HOSTS = ['*'] 

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# ------------------------------------------------------------------------------
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': dj_database_url.config(),
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
STATIC_ROOT = str(ROOT_DIR.path('static'))

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(ROOT_DIR.path('media'))

# CELERY CONFIGURATION
# ------------------------------------------------------------------------------
BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
