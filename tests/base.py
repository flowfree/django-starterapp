from os.path import join, dirname, abspath

from django.test import TestCase
from django.contrib.auth.models import User


FIXTURES_DIR = join(dirname(abspath(__file__)), 'fixtures')

class BaseTests(TestCase):
    fixtures = [
        join(FIXTURES_DIR, 'users.json'),
    ]

    def setUp(self):
        self.bob = User.objects.get(username='bob')
        self.alice = User.objects.get(username='alice')
