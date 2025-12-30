import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', "django-insecure-u1^0r$0fer02ex4nio2yfdc#q%a_@ie^_&jm%#=e4u20p^g6&9")

DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Auto-add Render's hostname + env override
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
if os.getenv('RENDER_EXTERNAL_HOSTNAME'):
    ALLOWED_HOSTS.append(os.getenv('RENDER_EXTERNAL_HOSTNAME'))
_raw = os.getenv('DJANGO_ALLOWED_HOSTS', '')
if _raw:
    ALLOWED_HOSTS.extend([h.strip() for h in _raw.split(',') if h.strip()])
ALLOWED_HOSTS.append('*')  # Temporary fallback

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap5",
    "dashboard",
    "accounts",
    "cases",
    "contacts",
    "contracts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Must be here for static
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ... (keep your TEMPLATES, WSGI_APPLICATION, etc. unchanged)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}
if os.getenv('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.parse(os.getenv('DATABASE_URL'))

# Static files fix for WhiteNoise
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")] if DEBUG else []
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"  # Non-manifest to avoid common 500

# Keep the rest of your file unchanged (Celery, email, etc.)
