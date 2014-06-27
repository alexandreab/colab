
from custom_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_HOST = ''
#EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')(jksdfhsjkadfhjkh234ns!8fqu-1186h$vuj'

SITE_URL = 'http://189.9.150.154'

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ('127.0.0.1', )

CONVERSEJS_BOSH_SERVICE_URL = 'http://localhost:5280/http-bind'

DATABASES['default']['PASSWORD'] = 'colab'
DATABASES['default']['HOST'] = '10.18.0.10'
DATABASES['trac']['PASSWORD'] = 'colab'
DATABASES['trac']['HOST'] = '10.18.0.10'

HAYSTACK_CONNECTIONS['default']['URL'] = 'http://10.18.0.9:8983/solr/'

COLAB_TRAC_URL = 'http://10.18.0.7:5000/trac/'
COLAB_CI_URL = 'http://localhost:8080/ci/'
COLAB_GITLAB_URL = 'http://127.0.0.1:8090/gitlab/'
#COLAB_GITLAB_URL = 'http://10.18.0.8:8090/gitlab/'

COLAB_REDMINE_URL = 'http://10.18.0.9:9080/redmine/'
COLAB_SVN_URL = 'http://10.18.0.7/repos/' 

CONVERSEJS_ENABLED = False

DIAZO_THEME = SITE_URL

ROBOTS_NOINDEX = True
