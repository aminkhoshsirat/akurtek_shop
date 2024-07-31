from django import forms
from .models import UserModel


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['profile_image', 'fullname', 'birth_date', 'email', 'state', 'city', 'address', 'post_code']


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=72)


class LoginSendForm(forms.Form):
    phone = forms.CharField(max_length=11)


class LoginActivationForm(forms.Form):
    phone = forms.CharField(max_length=11)
    code = forms.CharField(max_length=6)