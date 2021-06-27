from django.contrib.auth.forms import  AuthenticationForm
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Pass', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
