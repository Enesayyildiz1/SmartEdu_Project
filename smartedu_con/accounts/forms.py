from types import resolve_bases
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'First Name'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Password'
    }))

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'First Name'
    }))

    last_name=forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Last Name'
    }))

    username=forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Username'
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder':'Email'
    }))
    password1 =forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Password'
    }))
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Re-type  Password'
    }))
    class meta:
        model= User
        fields=['first_name','last_name','username','email','password1','password2']

"""
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs=
        {
            'class': 'form-control',
            'placeholder':'First Name'
        }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs=
        {
            'class': 'form-control',
            'placeholder':'Last Name'
        }))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs=
        {
            'class': 'form-control',
            'placeholder':'Email'
        }))
    number=forms.CharField(widget=forms.TextInput(
        attrs=
        {
            'class': 'form-control',
            'placeholder':'Number'
        }))
    message=forms.CharField(widget=forms.Textarea(attrs=
        {
            'class': 'form-control',
            'placeholder':'Message'
        }))
    class Meta:
        model=Contact
        fields=['first_name','last_name','email','number','message']"""