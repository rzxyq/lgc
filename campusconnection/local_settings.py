
import dj_database_url

DEBUG = True

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

if len(DATABASES['default']) == 0:
    DATABASES = {
        # local development settings
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'lgc',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
    }
}


