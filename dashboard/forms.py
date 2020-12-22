from django import forms
from .models import SubmitRequest
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder" : "Confirm Password"}))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder" : "Choose Password"}))
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Choose a username"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "First Name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Last Name"}))
    email = forms.CharField(widget= forms.EmailInput(attrs={"placeholder" : "Email Address"}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class UpdateUserForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Choose a username"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "First Name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Last Name"}))
    email = forms.CharField(widget= forms.EmailInput(attrs={"placeholder" : "Email Address"}))
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {"email":"Email"}

class SubmitRequestForm(forms.ModelForm):
    class Meta:
        model = SubmitRequest
        fields = "__all__"