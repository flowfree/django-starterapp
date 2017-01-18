from os.path import join, dirname, abspath

from django.test import TestCase
from django.contrib.auth.models import User


FIXTURES_DIR = join(dirname(abspath(__file__)), 'fixtures')
ASSETS_DIR = join(dirname(abspath(__file__)), 'assets')

class BaseTests(TestCase):
    fixtures = [
        join(FIXTURES_DIR, 'users.json'),
    ]

    def setUp(self):
        self.bob = User.objects.get(username='bob')
        self.alice = User.objects.get(username='alice')
        self.sample_image = open(join(ASSETS_DIR, 'sample_image.png'), 'rb')
        self.sample_textfile = open(join(ASSETS_DIR, 'lorem.txt'), 'rb')

    def tearDown(self):
        self.sample_image.close()
        self.sample_textfile.close()
