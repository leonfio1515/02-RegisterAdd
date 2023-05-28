from pathlib import Path
import dj_database_url
import os
from django.contrib.messages import constants as messages_error
####################################################################

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!5c34^=a9*t*hex^riq2x2cc7&itcdx$$t5qr0dc_5b26@5c5n'





#---------------APPS-------------------------------------#
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'DB',
    'Login',
    'widget_tweaks',
]


#---------------MIDDLEWARE-------------------------------------#
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'crum.CurrentRequestUserMiddleware',
]

ROOT_URLCONF = 'User_create.urls'


#---------------TEMPLATES-------------------------------------#

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates/Base',
            BASE_DIR / 'templates/View',
            BASE_DIR / 'templates/send_mail',
            BASE_DIR / 'Login/templates',
        ],
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

WSGI_APPLICATION = 'User_create.wsgi.application'


#--------------- Password Validation-----------------------#
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#---------------------- Regional Config------------------------#

LANGUAGE_CODE = 'es-la'

TIME_ZONE = 'America/Montevideo'

USE_I18N = True

USE_TZ = True


#-----------------Static Files--------------------------------#

STATIC_URL = 'static/'
MEDIA_URL = 'media-user/'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#--------------------Users----------------------------------------#

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
AUTH_USER_MODEL = 'DB.Users'


LOGIN_REDIRECT_URL = 'home'



#--------------------Send Mail----------------------------------------#

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "generic.test.send.mail@gmail.com"
EMAIL_HOST_PASSWORD = "dtsncmizdfasvars"


#--------------------BBDD----------------------------------------#
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
