"""
Django settings for advance_payment project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1t!_ndm$05$nikg$-nlcyd2e#zw9e&!zzv4g6@66z(3h$$jeab'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['adv-payment-jwt.herokuapp.com', '127.0.0.1', 'localhost']


# SMTP Configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'adv.payment.jwt@gmail.com'
EMAIL_HOST_PASSWORD = 'advancepaymentjwt2021'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "Lucas <adv.payment.jwt@gmail.com>"

ADMINS = [('Lucas', EMAIL_HOST_USER)]
MANAGERS = ADMINS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'crispy_forms',
    'apps.core',
    'apps.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'advance_payment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'advance_payment.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# PostgreSQL Heroku's Configuration
import dj_database_url

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JWT settings
AUTH_USER_MODEL = 'users.User'
CORS_ORIGIN_ALLOW_ALL = True        # Allows all front-end ports access
CORS_ALLOW_CREDENTIALS = True       # Allow front-end to get the cookies sent


# Celery & Redis Setup
CELERY_BROKER_URL = 'redis://:pff89bb7cf38c0fad11f761bd7a3e8cbbfb668222df31a61a5d542784b02bf3ff@ec2-23-20-238-97.compute-1.amazonaws.com:25060'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'


# Crispy Forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login Redirect
LOGIN_REDIRECT_URL = '/dashboard'
LOGIN_URL = '/login'
