from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignupForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def signup_user(request):
    if not request.user.is_authenticated:    
        if request.method == "POST":
            forms = SignupForm(request.POST)
            if forms.is_valid():
                forms.save() 
                request.session["message_log"] = True
                return redirect("login")
        else:
            forms = SignupForm()

        context = {"forms":forms}
        return render(request, "dashboard/signup.html", context)

    else:
        return redirect("login")

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            forms = AuthenticationForm(request=request, data=request.POST)
            if forms.is_valid():
                login_uname = forms.cleaned_data["username"]
                login_upass = forms.cleaned_data["password"]
                user = authenticate(username = login_uname, password = login_upass)

                if user is not None:
                    login(request, user)
                    return redirect("user_profile")
        else:
            if request.session["message_log"] == True:
                messages.success(request, "Your account has been created")
                request.session["message_log"] = False
                forms = AuthenticationForm()
            else:
                forms = AuthenticationForm()


        context = {"forms":forms}
        return render(request, "dashboard/login.html", context)
    else:
        return redirect("home")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        request.session["message_log"] = False
        return redirect("login")


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            forms = UpdateUserForm(request.POST, instance=request.user)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Your Profile has been Updated")
        
        else:
            forms = UpdateUserForm(instance=request.user)

        context = {"forms":forms}
        return render(request, "dashboard/user_profile.html", context)
    else:
        return redirect("login")