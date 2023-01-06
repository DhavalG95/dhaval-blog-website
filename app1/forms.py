from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Info(forms.ModelForm):
    class Meta:
        model = Form
        fields = "__all__"

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=125)
    last_name = forms.CharField(max_length=125)
    email = forms.EmailField(max_length=125)
    number = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','number','password1','password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"