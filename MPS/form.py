from django.forms import ModelForm

from django import forms


class UserInputForm(forms.Form):
    Name = forms.CharField(max_length=50)
    Region = forms.CharField(max_length=50, help_text='us/eu')
    Server = forms.CharField(max_length=50, help_text='No special characters')
