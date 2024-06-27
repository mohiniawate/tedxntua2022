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
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your apps here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tedxntua2022.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tedxntua2022.wsgi.application'

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



# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'