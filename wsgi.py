#Dotcloud only adds current to the python path
import sys
sys.path.append('django_project')

#This is needed to get into the right django 'context'
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings_deployment'

import django.core.handlers.wsgi
djangoapplication = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return djangoapplication(environ, start_response)
