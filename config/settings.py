

from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.contrib.messages import constants as messages


MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'bg-red-100',

}

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ml3b-x9e+*b5gd97f*_)iokb8c61qj(aen*_nj3&wpo^0$l70u'
DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'api',
    'blog',
    'page',
    'clients',
    'projects',
    'quotes',
    'services',
    'support',
    'tasks',
    'frontend',
    'backend',
    'compressor',
    'tinymce',
    'sorl.thumbnail',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_quill',
    'ckeditor',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'config.urls'

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    ('es', _('Español')),

]
LOCALE_PATHS = [BASE_DIR / 'locale']
CORS_ORIGIN_ALLOW_ALL = True

STATIC_URL = 'static/'
MEDIA_URL = '/upload/'
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR, 'static']
else:
    STATIC_ROOT = BASE_DIR/ 'static'
MEDIA_ROOT = BASE_DIR / 'upload'

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_FORMS = {
    'login': 'backend.forms.CustomLoginForm',
    'signup': 'backend.forms.CustomSignupForm',
    'reset_password': 'backend.forms.CustomResetPasswordForm',
    'change_password': 'backend.forms.CustomPasswordChangeForm'
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'gisysco.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'islamsaoudi@gisysco.com'
EMAIL_HOST_PASSWORD = 'Qwerty@2222'
EMAIL_USE_TLS = True

LOGIN_REDIRECT_URL = 'dashboard'
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT
CKEDITOR_CONFIGS = {
    'default': {
        # 'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}


# TINYMCE_DEFAULT_CONFIG = {
#         'selector': 'textarea',
#         'theme': 'silver',
#     # "width": '100%',
#         'mobile': {
#         'menubar': True
#     }
    
# }

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'text-gray-700 bg-gray-100 border-gray-500 dark:bg-gray-200',
    messages.INFO: 'text-blue-700 bg-blue-100 border-blue-500 dark:bg-blue-200',
    messages.SUCCESS: 'text-green-700 bg-green-100 border-green-500 dark:bg-green-200',
    messages.WARNING: 'text-yellow-700 bg-yellow-100 border-yellow-500 dark:bg-yellow-200',
    messages.ERROR: 'text-red-700 bg-red-100 border-red-500 dark:bg-red-200',

}
