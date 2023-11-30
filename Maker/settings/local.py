from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'supermercado',
        'USER': 'postgres',
        'PASSWORD': 'bel123',
        'HOST': 'localhost',
        'DATABASE_PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_ROOT = BASE_DIR / 'media'
#Use of send email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "gaunaabeltiago@gmail.com"
EMAIL_HOST_PASSWORD = "fxuj ejee dmlw cjls"

CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", "https://http2.mlstatic.com")
CSP_SCRIPT_SRC = ("'self'", "https://http2.mlstatic.com")


MERCADO_PAGO = {
    'client_id': '8342641464330530',
    'client_secret': 'B5W4oFxtSL01CbvPl4eUyBlZ4lxZoaB5',
}


MERCADOPAGO_PUBLIC_KEY = 'APP_USR-a4aff583-5735-4121-b959-786138c9e851'

NOTIFICATIONS_SOFT_DELETE = True
#Las notificaciones se eliminarán por completo de la base de datos cuando un usuario las marque como leídas o las elimine
NOTIFICATIONS_USE_JSONFIELD = True
#Se utilizará un campo JSONField para almacenar datos adicionales relacionados con las notificaciones

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
JAZZMIN_SETTINGS = {
    'site_header': "TRUE MAKER",
    'site_brad': "LETS GO",
    'site_logo': 'img/supermercado.png',
    'site_copyright': "True-maker",
    
    
}


