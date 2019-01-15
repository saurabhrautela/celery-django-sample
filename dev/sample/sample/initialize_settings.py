import os

try:
    # settings initialized from environment goes here
    SECRET_KEY_VALUE = os.environ['SECRET_KEY_VALUE']
    # Check if environment staging
    if os.environ['APP_ENVIRONMENT'] == 'staging':
        DEBUG_VALUE = os.environ['DEBUG_VALUE']
    else:
        DEBUG_VALUE = 'false'

    ALLOWED_HOSTS_VALUE = os.environ['ALLOWED_HOSTS_VALUE']

    DATABASE_NAME_VALUE = os.environ['DATABASE_NAME_VALUE']
    DATABASE_USER_VALUE = os.environ['DATABASE_USER_VALUE']
    DATABASE_PASSWORD_VALUE = os.environ['DATABASE_PASSWORD_VALUE']
    DATABASE_HOSTNAME_VALUE = os.environ['DATABASE_HOSTNAME_VALUE']
    DATABASE_PORT_VALUE = os.environ['DATABASE_PORT_VALUE']

    CELERY_BROKER_URL_VALUE = os.environ['CELERY_BROKER_URL_VALUE']
    CELERY_ACCEPT_CONTENT_VALUE = os.environ['CELERY_ACCEPT_CONTENT_VALUE']
    CELERY_RESULT_BACKEND_VALUE = os.environ['CELERY_RESULT_BACKEND_VALUE']
    CELERY_TASK_SERIALIZER_VALUE = os.environ['CELERY_TASK_SERIALIZER_VALUE']
except:
    # settings used for development
    SECRET_KEY_VALUE = 'z+4d!1k@ebw+a8hh-jc)ahaee5*grj2j$np34f_+6!v^n_rh=k'
    # Check to ensure it is not production environment
    DEBUG_VALUE = 'true'
    ALLOWED_HOSTS_VALUE = '*'

    DATABASE_NAME_VALUE = 'celery-demo'
    DATABASE_USER_VALUE = 'postgres-admin'
    DATABASE_PASSWORD_VALUE = 'password123'
    DATABASE_HOSTNAME_VALUE = 'localhost'
    DATABASE_PORT_VALUE = '5432'

    CELERY_BROKER_URL_VALUE = 'amqp://celerydemo:celerydemo@192.168.33.30:5672//'
    CELERY_ACCEPT_CONTENT_VALUE = 'json'
    CELERY_RESULT_BACKEND_VALUE = 'db+sqlite:///results.sqlite'
    CELERY_TASK_SERIALIZER_VALUE = 'json'
    try:
        env = 'development'
        env = os.environ['APP_ENVIRONMENT'].lower()
        raise
    except:
        if env == 'production' or env == 'staging':
            raise
