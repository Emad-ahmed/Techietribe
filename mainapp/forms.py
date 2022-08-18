from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from .models import Student
from django.utils.translation import gettext_lazy as _


class SignForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',  widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username',  'first_name', 'last_name', 'email')
        labels = {'email': "Email"}

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exists")

        return email


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id_no', 'first_name',
                  'last_name', 'email', 'password', 'cpassword']
        labels = {'cpassword': 'Confirm Password'}

        widgets = {
            'id_no': forms.TextInput(attrs={'placeholder': 'Id No'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'cpassword': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exists")

        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')
