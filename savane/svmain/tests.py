# Tests
# Copyright (C) 2010  Sylvain Beucler
#
# This file is part of Savane.
# 
# Savane is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# Savane is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.core import mail
from django.test import TestCase
from django.core.urlresolvers import reverse
import django.contrib.auth.models as auth_models
import re

class SimpleTest(TestCase):
    fixtures = [
        'license.yaml',
        'developmentstatus.yaml',
        ]

    def test_010_user_new(self):
        """
        Creates a new user (and tests templates)

        Sample long scenario.
        """
        response = self.client.get(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('registration_register'),
                                    {'username': 'test', 'email': 'test@test.tld',
                                     'password1': 'test', 'password2': 'test'})
        self.assertRedirects(response, reverse('registration_complete'))
        self.assertEqual(len(mail.outbox), 1)
        m = re.search(r'/([a-f0-9]{40})/', mail.outbox[0].body)
        self.assertTrue(m != None)
        hash = m.groups()[0]
        mail.outbox = []
        
        response = self.client.get(reverse('registration_activate', args=[hash]))
        self.assertRedirects(response, reverse('registration_activation_complete'))
        self.assertTrue(self.client.login(username='test', password='test'))
