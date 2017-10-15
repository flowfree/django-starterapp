from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from ..base import BaseTests


class TokenAuthenticationTests(BaseTests):
    def test_all_users_have_auth_token(self):
        self.assertIsNotNone(self.bob.auth_token.key)
        self.assertIsNotNone(self.alice.auth_token.key)

    def test_valid_login(self):
        response = self.client.post('/api-token-auth/', {
            'username': 'bob',
            'password': 's3cr3t',
        })

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content.decode('utf-8'), 
            {'token': self.bob.auth_token.key},
        )

        response = self.client.post('/api-token-auth/', {
            'username': 'alice',
            'password': 's3cr3t',
        })

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content.decode('utf-8'), 
            {'token': self.alice.auth_token.key},
        )

    def test_invalid_login(self):
        response = self.client.post('/api-token-auth/', {
            'username': 'bob',
            'password': 'xxx',
        })

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content.decode('utf-8'), {
            'non_field_errors': ['Unable to log in with provided credentials.']
        })


class UpdateProfileTests(BaseTests):
    def setUp(self):
        super().setUp()
        self.client.login(username='bob', password='s3cr3t')

    def test_login_required(self):
        self.client.logout()
        response = self.client.get('/user/profile/')

        self.assertRedirects(
            response, 
            '/user/login/?next=/user/profile/',
        )

    def test_render_the_correct_template(self):
        response = self.client.get('/user/profile/')

        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')

    def test_with_valid_data(self):
        response = self.client.post('/user/profile/', {
            'name': 'updated name',
            'email': 'bob222@example.com',
            'bio': 'updated bio',
            'website': 'https://example.com',
        }, follow=True)

        user = User.objects.get(username='bob')
        m = list(response.context['messages'])

        self.assertTrue(response.status_code, 200)
        self.assertEqual(len(m), 1)
        self.assertEqual(str(m[0]), 'Successfully updated your profile.')
        self.assertEqual(user.profile.name, 'updated name')
        self.assertEqual(user.email, 'bob222@example.com')
        self.assertEqual(user.profile.bio, 'updated bio')
        self.assertEqual(user.profile.website, 'https://example.com')

    def test_with_invalid_data(self):
        response = self.client.post('/user/profile/', {
            'name': '',
            'bio': '',
            'email': 'xxx',
            'website': 'yyy',
        })

        self.assertEqual(len(response.context['form'].errors), 2)
        self.assertFormError(
            response, 
            'form', 
            'email', 
            'Enter a valid email address.',
        )
        self.assertFormError(
            response, 
            'form', 
            'website',
            'Enter a valid URL.',
        )

    def test_reject_duplicated_email(self):
        response = self.client.post('/user/profile/', {
            'name': 'updated name',
            'email': 'alice@example.com',
            'bio': 'updated bio',
            'website': 'http://example.com',
        })

        self.assertEqual(len(response.context['form'].errors), 1)
        self.assertFormError(response, 'form', 'email',
            'This email is already used by other user.')


class ChangePasswordTests(BaseTests):
    def setUp(self):
        super().setUp()
        self.client.login(username='bob', password='s3cr3t')

    def test_login_required(self):
        self.client.logout()
        response = self.client.get('/user/change_password/')

        self.assertRedirects(
            response, 
            '/user/login/?next=/user/change_password/',
        )

    def test_render_the_correct_template(self):
        response = self.client.get('/user/change_password/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/change_password.html')

    def test_with_valid_data(self):
        response = self.client.post('/user/change_password/', {
            'current_password': 's3cr3t',
            'new_password': 'secret',
            'confirm_new_password': 'secret',
        }, follow=True)

        msg = list(response.context['messages'])

        self.assertTrue(len(msg), 1)
        self.assertEqual(str(msg[0]), 'Password successfully changed.')
        self.assertIsNotNone(authenticate(username='bob', password='secret'))

    def test_with_invalid_data(self):
        response = self.client.post('/user/change_password/', {
            'current_password': 'wrongpass',
            'new_password': 'xxx',
            'confirm_new_password': 'yyyyy',
        })

        self.assertEqual(len(response.context['form'].errors), 3)
        self.assertFormError(
            response, 
            'form', 
            'current_password',
            'Please enter the correct password',
        )
        self.assertFormError(
            response,
            'form',
            'new_password',
            'Ensure this value has at least 5 characters (it has 3).',
        )
        self.assertFormError(
            response,
            'form',
            'confirm_new_password',
            'This value should match with the new password',
        )
