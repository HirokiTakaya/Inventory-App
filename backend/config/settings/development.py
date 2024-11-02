from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app',
        'USER': 'root',
        'PASSWORD': 'new_password',
        'HOST': '127.0.0.1',  # または MySQL サーバーの IP アドレス
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}