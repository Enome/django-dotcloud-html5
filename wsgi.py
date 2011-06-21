import os
import socket
import sys

import django.core.handlers.wsgi

#Dotcloud only adds current to the python path
sys.path.append('django_project')

#This is needed to get into the right django 'context'
hostname = socket.gethostname()
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.{0}'.format(hostname)

djangoapplication = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return djangoapplication(environ, start_response)
