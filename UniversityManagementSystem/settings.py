import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMP_DIR=os.path.join(BASE_DIR,'managementApp/templates')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '33(*!!u8a(e%kq_i#p(j8hj=w)ujw=0v#))=69i6+9+f-s9j6+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#HEROKU LIVE PROJECT LINK
# ALLOWED_HOSTS = ["UniversityManagementSystem.herokuapp.com"]
ALLOWED_HOSTS = ["*"]

MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")

STATIC_URL="/static/"
STATIC_ROOT=os.path.join(BASE_DIR,"static")
# STATICFILES_DIRS = (os.path.join(BASE_DIR,"static"),)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'managementApp'
]

MIDDLEWARE = [
    #===Enable Only Making Project Live on Heroku==
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'managementApp.LoginCheckMiddleWare.LoginCheckMiddleWare'
]

ROOT_URLCONF = 'UniversityManagementSystem.urls'

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMP_DIR],
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

WSGI_APPLICATION = 'UniversityManagementSystem.wsgi.application'


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

STATIC_URL = '/static/'
AUTH_USER_MODEL="managementApp.CustomUser"
AUTHENTICATION_BACKENDS=['managementApp.EmailBackEnd.EmailBackEnd']

EMAIL_BACKEND="django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH=os.path.join(BASE_DIR,"sent_mails")

# EMAIL_HOST="smtp.gmail.com"
# EMAIl_PORT=587
# EMAIL_HOST_USER="GMAIL_EMAIL"
# EMAIL_HOST_PASSWORD="GMAIL PASSWORD"
# EMAIL_USE_TLS=True
# DEFAULT_FROM_EMAIL="Student management System <GMAIl_EMAIL>"
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR,'static'),
#     )
#Enable Only Making Project Live on Heroku
# STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage'
# import dj_database_url
# prod_db=dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)
