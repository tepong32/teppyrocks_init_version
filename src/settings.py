"""
Django settings for site_adminlte_trial project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.conf import settings # tried for email-sending pw-reset attempts

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "!4w%dze725mc^)w$b+*417fk+masts6659=lco-2jc*jm4va^$!5(ju" #os.environ.get('PROJWEB_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #os.environ.get('DEBUG_VALUE')

ALLOWED_HOSTS = ['thehideout.pythonanywhere.com', 'localhost']


# Application definition
# add the apps right away after creation to avoid headaches

INSTALLED_APPS = [
    # theme
    'adminlte3',
    'adminlte3_theme',

    # local apps / created by me
    'blog.apps.BlogConfig',
    'home.apps.HomeConfig',
    'lounge.apps.LoungeConfig',
    'users.apps.UsersConfig',
    'todo.apps.TodoConfig',
    'utilities.apps.UtilitiesConfig',   # not being used atm

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party apps // mostly for end-user rich-text editing
    'pagedown.apps.PagedownConfig',     # what's this for??
    
    'bootstrap_modal_forms',
    'crispy_forms',             # for better form-display formatting
    'markdown_deux',
    # 'pinax.announcements',      # announcements library # still checking out how to use this
    # 'pinax.templates',
    'bootstrapform',
    

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

ROOT_URLCONF = 'src.urls'

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

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")     # where we want django to save uploaded files
MEDIA_URL = '/media/'


CRISPY_TEMPLATE_PACK = 'bootstrap4'     # for the css of crispy forms


LOGIN_REDIRECT_URL = 'home'     # needed for the login.html success instance
LOGIN_URL = 'login'             # for the @login_required decorator on users/views.profile

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587 #587
EMAIL_USE_TLS = True


# TO USE THESE VARIABLES BELOW, USE ENVIRONMENT VARIABLES TO HIDE SENSITIVE INFO
# CHECK CoreyMs' Django TUTORIAL # 12 -- 14:20


EMAIL_HOST_USER = os.environ.get('WEBSITE_USER') # var for email username
EMAIL_HOST_PASSWORD = os.environ.get('WEBSITE_PASS') # var for email pw
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER # for email-sending pw-reset requests