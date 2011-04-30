# -*- coding: utf-8 -*-
import re

from freshen import *

from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.management import call_command
from django.conf import settings
from django.db.models import get_model
import os

#####################
## Setup/Teardown ##
###################

@Before
def before(sc):
    scc.client = Client()

@After
def after(sc):
    pass

#############
## GIVENS ##
###########

@Given('I am not logged in')
def logout():
    scc.client.logout()
    scc.session_cookie_after_logout = scc.client.cookies.get(settings.SESSION_COOKIE_NAME)

@Given('I am logged in')
def login():
    try:
        User.objects.get(username='foo')
    except User.DoesNotExist:
        scc.user = User.objects.create_user('foo', 'foo@bar', 'bar')

    scc.client.login(username='foo', password='bar')
    scc.session_cookie_after_login = scc.client.cookies.get(settings.SESSION_COOKIE_NAME)

############
## WHENS ##
##########

@When('I visit the url \'([^\']+)\'')
def get_the_url(url):
    scc.url = reverse(url)

@When('_I visit the url \'([^\']+)\'\s?(with the values: .+)?')
def get_the_url_with_parameters(url, values):
    scc.url = reverse(url, kwargs=values)


############
## THENS ##
##########

@Then('I should get status code \'(\d+)\'')
def assert_status_code(code):
    code = int(code)
    response = scc.client.get(scc.url)
    assert_equal( response.status_code , code )

@Then('I should see the template \'(.+)\'')
def assert_template_name(template):
    response = scc.client.get(scc.url)
    if hasattr(response, 'template_name'):
        assert_equal( response.template_name[0] , template )
        return

    assert False, 'Template was not found'
