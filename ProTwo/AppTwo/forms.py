from django import forms
from django.contrib.auth.models import User
from AppTwo.models import SignIn, UsesrProfileInfo

class NewUser(forms.ModelForm):
    class Meta():
        model = SignIn
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UsesrProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UsesrProfileInfo
        fields = ('portfolio_site', 'portfolio_pic')
