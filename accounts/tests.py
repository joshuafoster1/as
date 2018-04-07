# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import signup
# Create your tests here.

class SignUpTests(TestCase):
    def setup(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)


class SuccessfulSignUpTests(Testcase):
    def setup(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'password1': 'abcdefg1234',
            'password2': 'abcdefg1234'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')
