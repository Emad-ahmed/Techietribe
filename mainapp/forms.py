from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from .models import Student
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation


class SignForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',  widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username',  'first_name', 'last_name', 'email')

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

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError("Password Not Match")

        return password2


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id_no', 'first_name',
                  'last_name', 'email', 'password', 'cpassword']
        labels = {'cpassword': 'Confirm Password'}

        widgets = {
            'id_no': forms.NumberInput(attrs={'placeholder': 'Id No'}),
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

    def clean_id_no(self):
        id_no = self.cleaned_data['id_no']
        id_no = str(id_no)
        if len(id_no) != 10:
            raise forms.ValidationError("Student Id No is not valid")

        return id_no


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class StudentEditRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id_no', 'first_name',
                  'last_name', 'email']

        widgets = {
            'id_no': forms.TextInput(attrs={'placeholder': 'Id No'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),

        }


class TeacherEditRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
