from django import forms


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='Current password',
        min_length=5,
        widget=forms.PasswordInput(),
    )
    new_password = forms.CharField(
        label='New password',
        min_length=5,
        widget=forms.PasswordInput(),
    )
    confirm_new_password = forms.CharField(
        label='Confirm new password',
        min_length=5,
        widget=forms.PasswordInput(),
    )
    user = None

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        if self.user is None:
            raise Exception('The `user` parameter is required for ChangePasswordForm.')
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        value = self.cleaned_data['current_password']
        if not self.user.check_password(value):
            raise forms.ValidationError('Please enter the correct password')
        return value

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        pass1 = cleaned_data.get('new_password')
        pass2 = cleaned_data.get('confirm_new_password')
        if pass1 != pass2:
            self.add_error(
                'confirm_new_password', 
                'This value should match with the new password',
            )
        return cleaned_data