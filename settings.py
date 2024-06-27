'''Configuration for production mode'''
from .base import *  # pylint: disable=wildcard-import
from .env import abs_path, env_setting
import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# Set ALLOWED_HOSTS to the specific domains your application will serve
ALLOWED_HOSTS = env_setting('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Ensure DEBUG is set to False for production
DEBUG = False

# Add logging to file in production mode
LOGGING['handlers']['file'] = {
    'level': env_setting('LOG_LEVEL', 'INFO'),
    'class': 'logging.FileHandler',
    'filename': abs_path('logs', 'debug.log'),
    'formatter': 'verbose',
}

LOGGING['loggers']['']['handlers'].append('file')

STATICFILES_DIRS += (
    abs_path('bundles/dist'),
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '/',
        'STATS_FILE': abs_path('bundles', 'webpack-stats.prod.json'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tedexdb',
        'USER': 'admin',
        'PASSWORD': 'test1234',
        'HOST': 'db',  # Replace with correct hostname or IP
        'PORT': '3306',
    }
}
