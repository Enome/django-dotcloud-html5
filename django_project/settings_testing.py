#Test settings
from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
#Includes support for freshen and bdd style tests for unit tests
NOSE_ARGS = [r'-m', r'((?:^|[b_.-])(:?[Tt]est|When|should))', '--with-freshen',] 
