from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib import messages
from .forms import ContactForm
from dashboard.models import UserReview
from .models import Contact

# Create your views here.

def home(request):
    review_object = UserReview.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent")
            return redirect("/#contact")
    
    else:
        form = ContactForm()

    context = {"form":form, "review_object":review_object}
    return render(request, "home/index.html", context)

def signup_user(request):
    if not request.user.is_authenticated:    
        if request.method == "POST":
            forms = SignupForm(request.POST)
            if forms.is_valid():
                forms.save() 
                return redirect("login")
        else:
            forms = SignupForm()

        context = {"forms":forms}
        return render(request, "home/signup.html", context)

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
                    return redirect("home")
        else:
            forms = AuthenticationForm()

        context = {"forms":forms}
        return render(request, "home/login.html", context)
    else:
        return redirect("home")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")