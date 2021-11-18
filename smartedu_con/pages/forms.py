from django import forms
from . models import Contact


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
        fields=['first_name','last_name','email','number','message']