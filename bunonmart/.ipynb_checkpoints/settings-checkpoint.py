from pathlib import Path
import dj_database_url
from sqlalchemy import create_engine
from decouple import config, Csv, UndefinedValueError
from django.utils.translation import gettext_lazy as _
import os

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    SECRET_KEY = config('SECRET_KEY')
except UndefinedValueError:
    from django.core.management.utils import get_random_secret_key
    SECRET_KEY = get_random_secret_key()
DEBUG = True #config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# SECRET_KEY = "django-insecure-(_7=g=s986a#bnl03c+wm-68r2h-sup=mujaw*_net95by6y=6"
# DEBUG = True
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'bunonmart.local', 'bunonmart.onrender.com', 'bunonmart.com']

# Application definition

AUTH_USER_MODEL = 'accounts.CustomUser'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'shop',
    'accounts',
    'custom_order',
    'rosetta',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.microsoft',
]

SITE_ID = 1

ACCOUNT_FORMS = {
    'signup': 'accounts.forms.CustomUserCreationForm',
}

LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = "bunonmart.urls"
WSGI_APPLICATION = 'bunonmart.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "bunonmart.wsgi.application"

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'bunonmart_db',
#         'USER': 'postgres',
#         'PASSWORD': 'mugdho22',
#         'HOST': 'localhost',
#         'PORT': '5252',
#     }
# }

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('bn', _('Bengali')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_ZONE = 'Asia/Dhaka'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django.core.mail.backends.console.EmailBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGIN_METHODS = {'username', 'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Social Account Providers Settings (you must add real credentials for production)
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email'],
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
        ],
        'VERSION': 'v12.0'
    },
    'microsoft': {
        'SCOPE': ['User.Read'],
    },
}




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'WARNING',
    },
}

