from distutils.debug import DEBUG
from .settings_common import *

DEBUG=False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

# directories for static files
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

# AWS settings
AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_ID = os.environ.get('AWS_SES_SECRET_ACCESS_ID')
EMAIL_BACKEND = 'django_ses.SESBackend'

# logging
LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,

  # logger settings
  'loggers': {
    # logger for django
    'django': {
      'handlers': ['file'],
      'level': 'INFO',
    },
    # logger for diary application
    'diary':{
      'handlers': ['file'],
      'level': 'INFO',
    },
  },

  # handler settings
  'handlers':{
    'file': {
      'level': 'INFO',
      'class': 'logging.handlers.TImedRotatingFileHandler',
      'filename': os.path.join(BASE_DIR, 'logs/django.log'),
      'formatter': 'prod',
      'when': 'D', #log lotation span - day
      'interval':1, # period of time for logging - 1 day
      'backupCount': 7, # the number of files the system keeps
    },
  },

  # formatter settings
  'formatters': {
    'prod': {
      'format' : '\t'.join([
        '%(asctime)s',
        '[%(levelname)s]',
        '%(pathname)s(Line:%(lineno)d)',
        '%(message)s',
      ]),
    },
  }
}