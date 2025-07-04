from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda x: x.split(","))

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
]


THIRD_PARTY_APPS = [
    "django_hosts",
    "storages",
    "mptt",
]


LOCAL_APPS = [
    "data",
    "system",
    "photos",
    "home",
    "plants",
]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django_hosts.middleware.HostsRequestMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "prirodou.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "prirodou.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = config("LANGUAGE_CODE")
TIME_ZONE = config("TIME_ZONE")
USE_I18N = config("USE_I18N", cast=bool)
USE_TZ = config("USE_TZ", cast=bool)



STORAGES = {
    # media soubory přes SFTP
    "default": {
        "BACKEND": "storages.backends.sftpstorage.SFTPStorage",
        "OPTIONS": {
            "host": config("SFTP_STORAGE_HOST"),
            "params": {
                "username": config("SFTP_STORAGE_USER"),
                "key_filename": config("SFTP_STORAGE_KEYFILE", default=None),
                "port": config("SFTP_STORAGE_PORT", cast=int, default=22),
                "look_for_keys": config("SFTP_LOOK_FOR_KEYS", cast=bool, default=True),
                "allow_agent": config("SFTP_ALLOW_AGENT", cast=bool, default=False),
            },
            "root_path": config("SFTP_STORAGE_ROOT"),
            "base_url": config("SFTP_BASE_URL"),
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

MEDIA_URL=config("SFTP_BASE_URL")

STATIC_URL = config("STATIC_URL")
STATIC_ROOT = config("STATIC_ROOT")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_HOSTCONF = config("ROOT_HOSTCONF")
DEFAULT_HOST = config("DEFAULT_HOST")

LANGUAGES = [
    ('en', 'English'),
    ('cs', 'Čeština'),
]
