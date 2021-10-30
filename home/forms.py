from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    signup = forms.BooleanField(required=False)
    email = forms.EmailField(required=True)

    '''Stack Oveflow'''
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['signup'].label = "Receive Emails"

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'signup']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']
