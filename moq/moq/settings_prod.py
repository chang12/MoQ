from .settings import *
import os

if 'X_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['X_SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moq_db',
        'USER': 'chang12',
        'PASSWORD': 'vlfhrmfoald',
        'HOST': '127.0.0.1',
    },
}    
