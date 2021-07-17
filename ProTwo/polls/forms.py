from django import forms
from django.core import validators
from django.forms import fields
from polls import models
from django.contrib.auth.models import User


class register_form(forms.ModelForm):

    class Meta:
        model=models.Voter
        fields="__all__"


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','email','password')
        labels={
            'username':'Select User Name'

        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=models.UserProfileInfo
        fields=('profile_pic',)




