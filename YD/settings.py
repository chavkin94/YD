from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@b59rqx75a!d0)&_q!+0#8ysvj4417-!&0++y#jq7uj)ga&4(v'

DEBUG = True

#!
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'account.apps.AccountConfig',
    'organization.apps.OrganizationConfig',
    'master.apps.MasterConfig',
    'service.apps.ServiceConfig',

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

ROOT_URLCONF = 'YD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'YD.wsgi.application'

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

# AUTH_USER_MODEL = 'main.CustomUser'

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.CustomUser'

# LOGIN_URL = 'main/registration/login.html'
LOGIN_REDIRECT_URL = 'account:account'   #Маршрут по которому переходит после успешногот входа
# LOGOUT_REDIRECT_URL = 'main:index'   #Маршрут по которому переходит после выхода
# PASSWORD_RESET_TIMEOUT_DAYS = 3
# AUTHENTICATION_BACKENDS

# EMAIL_HOST = 'chavkin94@gmail.com'
# EMAIL_PORT = 1025
# EMAIL_HOST_USER = "Реальная почта"
# EMAIL_HOST_PASSWORD  = "Реальный пароль"
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True
# SERVER_EMAIL = EMAIL_HOST_USER
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
