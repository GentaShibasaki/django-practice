from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# loggin settings
LOGGING = {
  'version':1, 
  'disable_existing_loggers':False,

  # logger settings
  'loggers':{
    # logger which is used by Django
    'django' : {
      'handlers' : ['console'],
      'level': 'INFO'
    },
    # logger which is used by diary application
    'diary' :{
      'handlers':['console'],
      'level':'DEBUG',
    }
  },

  # handler settings
  'handlers' : {
    'console':{
      'level':'DEBUG',
      'class':'logging.StreamHandler',
      'formatter':'dev'
    }
  },

  # formetter settings
  'formatters':{
    'dev':{
      'format':'\t'.join([
        '%(asctime)s',
        '[%(levelname)s]',
        '%(pathname)s(Line:%(lineno)d)',
        '%(message)s'
      ])
    }
  }
}

# email settings

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# media settings

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')