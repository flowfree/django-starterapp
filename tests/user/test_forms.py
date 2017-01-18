import inspect
from django.test import TestCase

from apps.user.forms import ChangePasswordForm

from ..base import BaseTests


class ChangePasswordFormTests(BaseTests):
    def test_form_should_require_user_parameter(self):
        try:
            form = ChangePasswordForm()
            self.fail('Should raise Exception here.')
        except KeyError: 
            pass
        try:
            form = ChangePasswordForm(user=self.bob)
        except KeyError:
            self.fail('Should not raise Exception here.')

    def test_form_should_define_correct_fields(self):
        form = ChangePasswordForm(user=self.bob)

        for f in ['current_password', 'new_password', 'confirm_new_password']:
            self.assertTrue(f in form.fields)
            self.assertIsNotNone(form.fields[f])

    def test_with_invalid_data(self):
        data = dict(
            current_password='xxxxx',
            new_password='yyy',
            confirm_new_password='zzzzz',
        )
        form = ChangePasswordForm(data, user=self.bob)

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
        self.assertEqual(form.errors['current_password'], 
            ['Please enter the correct password'])
        self.assertEqual(form.errors['new_password'],
            ['Ensure this value has at least 5 characters (it has 3).'])
        self.assertEqual(form.errors['confirm_new_password'],
            ['This value should match with the new password'])

    def test_with_valid_data(self):
        data = dict(
            current_password='s3cr3t',
            new_password='secret',
            confirm_new_password='secret',
        )
        form = ChangePasswordForm(data, user=self.bob)

        self.assertTrue(form.is_valid())
