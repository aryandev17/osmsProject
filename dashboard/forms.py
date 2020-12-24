from django import forms
from .models import SubmitRequest
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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
    request_info = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Request Info"}))
    description = forms.CharField(widget= forms.Textarea(attrs={"placeholder" : "Description"}))
    name = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Your Name"}))
    address_line_1 = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Address Line 1"}))
    address_line_2 = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Address Line 2"}))
    city = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "City"}))
    state = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "State"}))
    zip_code = forms.CharField(widget= forms.NumberInput(attrs={"placeholder" : "Zip"}))
    mobile = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Mobile"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder" : "Email"}))
    date = forms.DateTimeField(widget= forms.DateInput(attrs={"type":"date"}))

    class Meta:
        model = SubmitRequest
        fields = "__all__"

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder" : "Old Password"}))
    new_password1 = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder" : "Choose New Password"}))
    new_password2 = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder" : "Confirm New Password"}))
    class Meta:
        fields = "__all__"