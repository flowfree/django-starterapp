import os
import dj_database_url
from .production import *

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

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_ROOT = str(ROOT_DIR.path('static'))

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(ROOT_DIR.path('media'))
