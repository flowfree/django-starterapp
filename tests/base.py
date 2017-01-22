from os.path import join, dirname, abspath

from django.test import TestCase
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress


# Django testing assertions:
# assertEqual
# assertRaises
# assertRedirects
# assertTrue
# assertRaisesMessage
# assertFieldOutput
# assertFormError
# assertFormsetError
# assertContains
# assertNotContains
# assertHTMLEqual
# assertHTMLNotEqual
# assertTemplateUsed
# assertTemplateNotUsed
# assertRedirects
# assertXMLEqual
# assertXMLNotEqual
# assertInHTML
# assertJSONEqual
# assertJSONNotEqual
# assertQuerysetEqual
# assertNumQueries


FIXTURES_DIR = join(dirname(abspath(__file__)), 'fixtures')
ASSETS_DIR = join(dirname(abspath(__file__)), 'assets')

class BaseTests(TestCase):
    def setUp(self):
        self.sample_image = open(join(ASSETS_DIR, 'sample_image.png'), 'rb')
        self.sample_textfile = open(join(ASSETS_DIR, 'lorem.txt'), 'rb')

        self.bob = self.create_user('bob', 's3cr3t')
        self.alice = self.create_user('alice', 's3cr3t')

    def tearDown(self):
        self.sample_image.close()
        self.sample_textfile.close()

    def create_user(self, username, password):
        user = User.objects.create_user(
            username, 
            '%s@example.com' % username, 
            password,
        )
        EmailAddress.objects.create(
            user=user, 
            email=user.email, 
            verified=True,
        )
        return user
