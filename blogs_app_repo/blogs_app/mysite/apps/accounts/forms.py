from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from captcha.fields import CaptchaField
from django.contrib import messages


class UserSignupForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=21)
    email = forms.EmailField(required=True, max_length = 75)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError("This email has already been registered.")
        return email


class UserUpdateForm(forms.ModelForm):
    # username = forms.CharField(required=True, max_length=21)
    #email = forms.EmailField(required=True, max_length = 75)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()
        if user_count > 1:
            raise forms.ValidationError("This email has already been registered.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_count = User.objects.filter(username=username).count()
        if user_count > 1:
            raise forms.ValidationError("This username has already been registered.")
        return username

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'info']
