from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfoForm

class UserForm(forms.ModelForm):
    passwords = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model =  UserProfileInfoForm
        fields = ('portfolio_site','profile_pic')
