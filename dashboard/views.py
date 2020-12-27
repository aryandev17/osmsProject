from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import SignupForm, UpdateUserForm, SubmitRequestForm, ChangePasswordForm, AssignTechnicianForm
from .models import ServiceStatus, SubmitRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import get_user_model

# Create your views here.

# ************* LOGIN SIGNUP VIEW *************************

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

                    if request.user.is_superuser:
                        return redirect("admin_dashboard")
                    else:
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

# ************* USER VIEW *************************

def user_profile(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            if request.method == "POST":
                forms = UpdateUserForm(request.POST, instance=request.user)
                if forms.is_valid():
                    forms.save()
                    messages.success(request, "Your Profile has been Updated")
            
            else:
                forms = UpdateUserForm(instance=request.user)

            context = {"forms":forms}
            return render(request, "dashboard/user/user_profile.html", context)
        else:
            return redirect("home")
    else:
        return redirect("login")

def submit_request(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            if request.method == "POST":
                forms = SubmitRequestForm(request.POST)
                if forms.is_valid():
                    submit_request_object = forms.save()
                    serial_no = submit_request_object.serial_no
                    service = ServiceStatus(service_id=serial_no, status_description="Your Request is in Process")
                    service.save()
                    forms = SubmitRequestForm
                    messages.success(request, "Your Request has been Submited. Your Service Id is ", extra_tags= str(serial_no))
            else:
                forms = SubmitRequestForm()

            context = {"forms":forms}
            return render(request, "dashboard/user/submit_request.html", context)
        else:
            return redirect("home")
    else:
        return redirect("login")

def service_status(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            if request.method == "POST":
                service_id = request.POST.get("service_id")
                service_status = ServiceStatus.objects.filter(service_id=service_id)

                context = {"status":service_status}
                return render(request, "dashboard/user/service_status.html", context)
            
            else:
                return render(request, "dashboard/user/service_status.html")
        else:
            return redirect("home")
    else:
        return redirect("login")

def change_password(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            if request.method == "POST":
                forms = ChangePasswordForm(request.user, request.POST)
                if forms.is_valid():
                    forms.save()
                    update_session_auth_hash(request, request.user)
                    messages.success(request, "Your Password has been change successfully")

            else:
                forms = ChangePasswordForm(request.user)

            context = {"forms":forms}
            return render(request, "dashboard/user/change_password.html", context)
        else:
            return redirect("home")
    else:
        return redirect("login")

# ************* ADMIN VIEW *************************

def admin_dashboard(request):
    if request.user.is_superuser:
        requests_object = SubmitRequest.objects.all()
        User = get_user_model()
        users = User.objects.all()
        count_requests = len(requests_object)
        context = {"count_requests":count_requests, "users":users}
        return render(request, "dashboard/admin/admin_dashboard.html", context)
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def admin_requests(request):
    if request.user.is_superuser:
        requests_object = SubmitRequest.objects.all()
        if request.method == "POST":
            request_id = request.POST.get("id")
            request_object2 = SubmitRequest.objects.filter(serial_no= request_id).first()
            forms = AssignTechnicianForm(request.POST)
            context = {"forms":forms, "requests_object":requests_object, "request_id":request_id, "request_object2":request_object2}
            if forms.is_valid():
                forms.save()
                delete_request = SubmitRequest.objects.filter(serial_no=request.POST.get("request_id")).first()
                print(delete_request)
                delete_request.delete()
                return redirect("admin_requests")

        else:
            forms = AssignTechnicianForm()
            context = {"forms":forms, "requests_object":requests_object}
        

    return render(request, "dashboard/admin/admin_requests.html", context)

def assigned_order(request):
    return render(request, "dashboard/admin/assigned_order.html")