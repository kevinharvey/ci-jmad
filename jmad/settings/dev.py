from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party stuff
    'authtools',

    # JMAD apps
    'tunes',

    # Dev stuff
    'django_tdd',
)

