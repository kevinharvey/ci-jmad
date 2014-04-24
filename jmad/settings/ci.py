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
    'people',
    'tunes',
    
    # CI stuff
    'django_jenkins',
)

# Tasks to run in Jenkins
JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.run_pep8',
)

# Tell Jenkins what apps to work on
PROJECT_APPS = (
    'people',
    'tunes',
)
