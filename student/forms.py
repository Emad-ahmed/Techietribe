from cProfile import label
from urllib import request

from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from django.core import validators
from django.utils.translation import gettext_lazy as _

from student.models import CommentMain


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentMain
        fields = ('comment', )
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
