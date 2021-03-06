#encoding:utf-8
"""
Django settings for centrointernet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#import dj_database_url

BASE_DIR        = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

SECRET_KEY = 'rutry8q@x(^7szp-+vo4!7#k119#&e2tdgs&)n)t4cxj)h))lz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
#CSRF_COOKIE_SECURE =  True
#SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
CSRF_COOKIE_HTTPONLY = True


X_FRAME_OPTIONS = 'DENY'

LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'Chile/Continental'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Redirect when login is correct.
LOGIN_REDIRECT_URL = "/inicio"
# Redirect when login is not correct.
LOGIN_URL = '/'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Allow all host headers
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'centrointernet',
    'facturacion',
    'problemas',
    'clientes',
    'pagos',
    'bootstrap3_datetime',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'centrointernet.urls'
WSGI_APPLICATION = 'centrointernet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Parse database configuration from $DATABASE_URL
#DATABASES= {}
#DATABASES['default'] =  dj_database_url.config(default=os.environ['DATABASE_URL'])


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db-centrointernet.sqlite3'),
    }
}

"""
 DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', 
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
"""


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    "django.core.context_processors.media",
    'django.core.context_processors.static',
)


TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_URL = '/static/'
STATIC_ROOT = ''


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Configuraciones para enviar mails
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'testcentrointernet@gmail.com'
EMAIL_HOST_PASSWORD = 'holamundo1313'
EMAIL_PORT = 587

PATH='/home/jm/Facturacion'