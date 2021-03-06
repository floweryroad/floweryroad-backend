import json
from django.conf import settings
from .base import *

CONFIG_SECRET_DIR = os.path.join(BASE_DIR, '.credential')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'credentials.json')
config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())

DEBUG = False

SECRET_KEY = config_secret['SECRET_KEY']

ROOT_URLCONF = 'floweryroad.urls.production'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'ec2-15-164-210-94.ap-northeast-2.compute.amazonaws.com',
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://floweryroad.s3-website.ap-northeast-2.amazonaws.com"
]

#AWS SETTING
AWS_ACCESS_KEY_ID = config_secret['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret['aws']['s3_bucket_name']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'

#Storage setting
DEFAULT_FILE_STORAGE = 'floweryroad.settings.storage_config.MediaStorage'
STATICFILES_STORAGE = 'floweryroad.settings.storage_config.StaticStorage'
MEDIAFILES_LOCATION = 'media'
STATICFILES_LOCATION = 'static'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config_secret['db']['NAME'],
        'USER': config_secret['db']['USER'],
        'PASSWORD': config_secret['db']['PASSWORD'],
        'HOST': config_secret['db']['HOST'],
        'PORT': config_secret['db']['PORT'],
    }
}
