"""
Django settings for around_the_world project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import django_heroku
import environ
import os
from pathlib import Path

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'around-the-world1'

# from dotenv import load_dotenv
environ.Env()
environ.Env.read_env()

# load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://around-the-world.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'main_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'toolbar_Custom',
        'height': 300,
        'width': 800,
        'autoParagraph': True,
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['NumberedList', 'BulletedList', 'Blockquote'],
            ['Link', 'Unlink', 'Anchor'],
            ['RemoveFormat', 'Source'],
            ['Maximize', 'ShowBlocks'],
            '/',
            ['Styles', 'Format'],
            ['TextColor', 'BGColor'],
            ['Image', 'Table', 'HorizontalRule'],
            ['Smiley', 'SpecialChar'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ],
        'stylesSet': [
            {'name': 'Red Title', 'element': 'span', 'styles': {'color': 'red'}},
            {'name': 'Blue Title', 'element': 'span', 'styles': {'color': 'blue'}},
            {'name': 'Warning', 'element': 'span', 'styles': {
                'background-color': '#FFC107', 'padding': '1rem', 'border-radius': '4px'}},
            {'name': 'Quote', 'element': 'span', 'styles': {
                'background-color': 'yellow', 'font-style': 'italic'}},
            {'name': 'Code', 'element': 'span', 'styles': {
                'background-color': '#F7F7F7', 'font-family': 'monospace', 'font-size': '1em'}},
            {'name': 'Big', 'element': 'span', 'styles': {'font-size': 'larger'}},
            {'name': 'Small', 'element': 'span',
                'styles': {'font-size': 'smaller'}},
            {'name': 'Smiley', 'element': 'img', 'styles': {'border': 'none'}},
            {'name': 'Thumbnail', 'element': 'img', 'styles': {'border': '1px solid #ddd',
                                                               'border-radius': '4px', 'padding': '5px', 'width': '150px'}},
            {'name': 'Green Subtitle', 'element': 'span', 'styles': {
                'color': 'green', 'font-size': '1.25em'}},
            {'name': 'Highlighted', 'element': 'span',
             'styles': {'background-color': '#FFFF00'}},
            {'name': 'Uppercase', 'element': 'span',
             'styles': {'text-transform': 'uppercase'}},
            {'name': 'Bigger', 'element': 'span', 'styles': {'font-size': '2em'}},
            {'name': 'Smaller', 'element': 'span',
             'styles': {'font-size': '0.5em'}},
            {'name': 'Align left', 'element': ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
                'attributes': {'class': 'align-left'}},
            {'name': 'Align center', 'element': ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
                'attributes': {'class': 'align-center'}},
            {'name': 'Align right', 'element': ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
                'attributes': {'class': 'align-right'}},
        ],
        'format_tags': 'p;h1;h2;h3;h4;h5;h6;pre;address;div',
        'contentsCss': '/static/css/style.css',
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'around_the_world.urls'

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

WSGI_APPLICATION = 'around_the_world.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news',
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
LOGIN_REDIRECT_URL = '/about/'
LOGOUT_REDIRECT_URL = '/about/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Configure Django to work within heroku production environment

django_heroku.settings(locals())
