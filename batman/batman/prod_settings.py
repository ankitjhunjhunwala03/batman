# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'batman',
        'USER': 'admingpdwznh',
        'PASSWORD': 'cl-X9_WuMZAS',
        'HOST': 'postgresql://$OPENSHIFT_POSTGRESQL_DB_HOST:$OPENSHIFT_POSTGRESQL_DB_PORT',
        'PORT': '',
    }
}
