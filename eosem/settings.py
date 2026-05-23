from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv()

# 1. RUTAS BASE
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. SEGURIDAD (Configuración de desarrollo)
SECRET_KEY = 'django-insecure-g%y#^(y3zyfu6z-22gj!89a$*t*ufbi7%03s3z8=h)2=uh=eq0'
DEBUG = True
ALLOWED_HOSTS = ["*"]

# 3. APLICACIONES
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',  # Tu aplicación principal
]

# 4. MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eosem.urls'

# 5. TEMPLATES (Configurado para tu carpeta dashboard/templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "dashboard" / "templates"], 
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

WSGI_APPLICATION = 'eosem.wsgi.application'

# 6. BASE DE DATOS (SQLite)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME"),          
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),          
    }
}

# 7. VALIDACIÓN DE CONTRASEÑAS
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 8. INTERNACIONALIZACIÓN (Configurado para Colombia)
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# 9. ARCHIVOS ESTÁTICOS (Imágenes, CSS, JS)
STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Esta configuración permite que Django encuentre la carpeta static dentro de dashboard
STATICFILES_DIRS = [
    BASE_DIR / "dashboard" / "static",
]

# 10. OTROS
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de Redirección de Login
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'