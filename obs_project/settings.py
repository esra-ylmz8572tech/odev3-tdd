"""Yerel ders çalışması için veritabanı gerektirmeyen Django ayarları."""
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "odev3-yalnizca-yerel-gelistirme-icin"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]
INSTALLED_APPS = ["students"]
MIDDLEWARE = []
ROOT_URLCONF = "obs_project.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": []},
    }
]
WSGI_APPLICATION = "obs_project.wsgi.application"
DATABASES = {}
LANGUAGE_CODE = "tr-tr"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
