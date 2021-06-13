from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields
from .models import Profile

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  first_name = forms.CharField(label='First Name', max_length=30)
  last_name = forms.CharField(label='Last Name', max_length=30)
 
  class Meta: 
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['email']


class ProfileUpdateFrom(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image', 'dob', 'gender', 'occupation', 'bio', 'country', 'public_key']