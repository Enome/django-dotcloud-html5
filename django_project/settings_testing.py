#Test settings
from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [r'-m', r'((?:^|[b_.-])(:?[Tt]est|describe|When|should|it))' ] 
SOUTH_TESTS_MIGRATE = False
