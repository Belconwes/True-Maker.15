from pathlib import Path
from django.contrib import auth


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i0n&$uz4gf(nawukhrdo6kc2=%(@kyvxftl*ksinuf2ocybm71'

# # Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django_light',
    'admin_tools_stats',  
    'django_nvd3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Locals apps
    'notifications',
    'Aplications.Usuarios',
    'Aplications.departamentos',
    'Aplications.productos',
    'Aplications.carrito',
    'Aplications.pedido',
    'Aplications.proveedor',
    'Aplications.descuentos',
    'fontawesomefree',
    'crispy_forms',
    'crispy_bootstrap5',
    'mercadopago',
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5'
AUTH_USER_MODEL = 'Usuarios.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Maker.urls'

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
                 'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'Maker.wsgi.application'
