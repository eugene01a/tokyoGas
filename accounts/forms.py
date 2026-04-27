from django import forms
from .models import CustomUser, Pref
from .validators import (
    validate_username,
    validate_email,
    validate_password,
    validate_tel,
    validate_pref,
)


class UserRegistrationForm(forms.ModelForm):
    # Form used for server-side registration and validation.
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    pref = forms.IntegerField(required=True, label='Prefecture')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'tel', 'pref']

    def clean_username(self):
        return validate_username(self.cleaned_data.get('username'))

    def clean_email(self):
        return validate_email(self.cleaned_data.get('email'))

    def clean_password(self):
        return validate_password(self.cleaned_data.get('password'))

    def clean_tel(self):
        return validate_tel(self.cleaned_data.get('tel'))

    def clean_pref(self):
        return validate_pref(self.cleaned_data.get('pref'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
