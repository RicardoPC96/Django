from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test-2',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)

STATIC_URL = '/static/'
DEBUG = True
