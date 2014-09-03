
from custom_settings import *

DEBUG = False
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

SITE_URL = 'http://104.131.28.60'
BROWSERID_AUDIENCES = [SITE_URL, SITE_URL.replace('https', 'http')]

ALLOWED_HOSTS = ['104.131.28.60']

INTERNAL_IPS = ('127.0.0.1', )

CONVERSEJS_BOSH_SERVICE_URL = 'http://localhost:5280/http-bind'

DATABASES['default']['PASSWORD'] = 'colab'
DATABASES['default']['HOST'] = 'localhost'

TRAC_ENABLED = False

if TRAC_ENABLED:
    from trac_settings import *
    DATABASES['trac'] = TRAC_DATABASE
    DATABASES['trac']['PASSWORD'] = 'colab'
    DATABASES['trac']['HOST'] = 'localhost'

HAYSTACK_CONNECTIONS['default']['URL'] = 'http://localhost:8983/solr/'

COLAB_TRAC_URL = 'http://localhost:5000/trac/'
COLAB_CI_URL = 'http://localhost:8080/ci/'
COLAB_GITLAB_URL = 'http://localhost:8090/gitlab/'
COLAB_REDMINE_URL = 'http://localhost:9080/redmine/'

CONVERSEJS_ENABLED = False

DIAZO_THEME = SITE_URL

ROBOTS_NOINDEX = True