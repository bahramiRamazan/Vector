from django import forms
from django.contrib.auth import get_user_model
from django_registration.forms import RegistrationForm


class SignupForm(RegistrationForm):
    """user signup form"""
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['email','name','mobil']


class LoginForm(forms.Form):
    """user login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
