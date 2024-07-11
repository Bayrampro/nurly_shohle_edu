from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(label='Parol', widget=forms.PasswordInput())


class FeedbackForm(forms.ModelForm):
    user = forms.CharField(label='Ady', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Hat', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField(label="Men adam")

    class Meta:
        model = Feedback
        fields = ['user', 'email', 'subject']
