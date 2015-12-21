"""
Django settings for campusconnection project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k9ahz9u+yt773iy*5rhincg12l8&5e+o5kba981r(!(_3kzrib'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.cucampusconnection.com','127.0.0.1']

ADMINS = (
    ('jimmychen', 'jsc349@cornell.edu'),
)
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'static_content',
    'newstudent',
    'upperclassman',
    'selection',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'campusconnection.urls'

WSGI_APPLICATION = 'campusconnection.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
  'default' : {
    'ENGINE' : 'django.db.backends.mysql',
    'NAME' : 'heroku_700535e64cd6917',
    'HOST' : 'us-cdbr-iron-east-01.cleardb.net',
    'PORT' : '',
    'USER' : 'b4002dcc6606d1',
    'PASSWORD' : 'f5ddc02c',
  }
}


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),

# )

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# EMAIL_HOST should be set to whatever host name your mail server is on.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

DEFAULT_FROM_EMAIL = 'letsgetcoffeecornell@gmail.com'
EMAIL_HOST_USER = 'letsgetcoffeecornell@gmail.com'
EMAIL_HOST_PASSWORD = 'Blakebarr'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
SERVER_EMAIL = 'django@letsgetcoffeecornell@gmail.com'

####Heruko####
#############
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

try:
    from local_settings import *
except ImportError:
    pass
