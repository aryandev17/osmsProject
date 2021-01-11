from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import SignupForm, UpdateUserForm, SubmitRequestForm, ChangePasswordForm, AssignTechnicianForm, AddTechnicianForm, WorkReportForm
from home.forms import UserReviewForm
from .models import ServiceStatus, SubmitRequest, AssignTechnician, TechnicianList, UserProfilePicture, UserReview
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
                # request.session["message_log"] = True
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
                    messages.error(request, "Check your username and password again !!")
            else:
                messages.error(request, "Check your username and password again !!")
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
            user_image_object = UserProfilePicture.objects.filter(user=request.user).first()
            if request.method == "POST":
                forms = UpdateUserForm(request.POST, instance=request.user)

                if forms.is_valid():
                    profile_picture = request.FILES.get("profile_picture")
                    if profile_picture:
                        if user_image_object is not None:
                            user_image_object.profile_picture = profile_picture
                            user_image_object.save(update_fields = ["profile_picture"])
                        else:
                            user_profile_picture = UserProfilePicture(user=request.user, profile_picture=profile_picture)
                            user_profile_picture.save()

                    forms.save()
                    messages.success(request, "Your Profile has been Updated")         
            else:
                forms = UpdateUserForm(instance=request.user)

            context = {"forms":forms, "user_image_object":user_image_object}
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

def review(request):
    user_details_object = UserProfilePicture.objects.get(user=request.user)
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            if request.method == "POST":
                forms = UserReviewForm(request.POST)
                if forms.is_valid():
                    review = forms.cleaned_data["review"]
                    review_title = forms.cleaned_data["review_title"]
                    user_review_object = UserReview(user_details=user_details_object, review=review, review_title=review_title)
                    user_review_object.save()
                    # review_message = "Your Review Has been Submitted"
                    # request.session["review_message"] = review_message
                    return redirect("review")
            else:
                # if "review_message" in request.session:
                #     forms = UserReviewForm()
                #     messages.success(request, request.session["review_message"])
                # else:                  
                forms = UserReviewForm()
            context = {"forms":forms}
            return render(request, "dashboard/user/review.html", context)
        else:
            return redirect("home")
    else:
        return redirect("login")

# ************* ADMIN VIEW *************************

def admin_dashboard(request):
    if request.user.is_superuser:
        requests_object = SubmitRequest.objects.all()
        assigned_order_object = AssignTechnician.objects.all()
        technicians_list_object = TechnicianList.objects.all()
        User = get_user_model()
        users = User.objects.all()
        count_requests = len(requests_object)
        count_assigned = len(assigned_order_object)
        count_technicians = len(technicians_list_object)
        context = {"count_requests":count_requests, "users":users, "count_assigned":count_assigned, "count_technicians":count_technicians}
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
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def assigned_order(request):
    if request.user.is_superuser:
        assigned_order_object = AssignTechnician.objects.all()
        context = {"assigned_orders":assigned_order_object}
        return render(request, "dashboard/admin/assigned_order.html", context)
    
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def delete_assigned_order(request, request_id):
    if request.user.is_superuser:
        assigned_order_request = AssignTechnician.objects.filter(request_id=request_id).first()
        assigned_order_request.delete()
        return redirect("assigned_order")

    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def view_assigned_order(request, request_id):
    if request.user.is_superuser:
        assign_order_object = AssignTechnician.objects.filter(request_id=request_id).first()
        context = {"assign_order_object":assign_order_object}
        return render(request, "dashboard/admin/view_assigned_order.html", context)
    
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def technician_list(request):
    if request.user.is_superuser:
        technicians_list = TechnicianList.objects.all()

        context = {"technicians_list":technicians_list}
        return render(request, 'dashboard/admin/technician_list.html', context)
    
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def add_technician(request, employee_id):
    if request.user.is_superuser:
        if request.method == "POST":
            if employee_id == 0:
                forms = AddTechnicianForm(request.POST)
            else:
                add_technician_object = TechnicianList.objects.filter(employee_id=employee_id).first()
                forms = AddTechnicianForm(request.POST, instance= add_technician_object)

            if forms.is_valid():
                forms.save()
                messages.success(request, "Employee Added Succesfully")
                return redirect("technician_list")
        
        else:
            if employee_id == 0:
                forms = AddTechnicianForm()
            else:
                add_technician_object = TechnicianList.objects.filter(employee_id=employee_id).first()
                forms = AddTechnicianForm(instance= add_technician_object)

        context = {"forms":forms, "employee_id":employee_id}

        return render(request, "dashboard/admin/add_technician.html", context)
    
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def delete_technician(request, employee_id):
    if request.user.is_superuser:
        delete_technician_object = TechnicianList.objects.get(employee_id=employee_id)
        delete_technician_object.delete()
        return redirect("technician_list")
    
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def work_report(request):
    if request.user.is_superuser:
        if request.method == "POST":
            forms = WorkReportForm(request.POST)
            context = {"forms":forms}
            if forms.is_valid():
                start_date = forms.cleaned_data["start_date"]
                end_date = forms.cleaned_data["end_date"]
                work_report_object = AssignTechnician.objects.filter(date__range = (start_date, end_date))
                context = {"forms":forms, "work_report_object":work_report_object}
            else:
                print("Main hoon else")
        
        else:
            forms = WorkReportForm()
            print("Main Hoon without Post")
            context = {"forms":forms}
        return render(request, "dashboard/admin/work_report.html", context)
    
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def admin_edit_profile(request):
    if request.user.is_superuser:
        admin_image_object = UserProfilePicture.objects.filter(user=request.user).first()
        if request.method == "POST":
            forms = UpdateUserForm(request.POST, instance=request.user)

            if forms.is_valid():
                profile_picture = request.FILES.get("profile_picture")
                if profile_picture:
                    if admin_image_object is not None:
                        admin_image_object.profile_picture = profile_picture
                        admin_image_object.save(update_fields = ["profile_picture"])
                    else:
                        admin_profile_picture = UserProfilePicture(user=request.user, profile_picture=profile_picture)
                        admin_profile_picture.save()

                forms.save()
                messages.success(request, "Your Profile has been Updated")
                # return redirect("admin_edit_profile")
        else:
            forms = UpdateUserForm(instance=request.user)

        context = {"forms":forms, "admin_image_object":admin_image_object}
        return render(request, "dashboard/admin/admin_edit_profile.html", context)
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")

def admin_change_password(request):
    if request.user.is_superuser:
        if request.method == "POST":
            forms = ChangePasswordForm(request.user, request.POST)
            if forms.is_valid():
                forms.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, "Your Password has been change successfully")
        
        else:
            forms = ChangePasswordForm(request.user)
            print(forms)
        
        context = {"forms":forms}

        return render(request, "dashboard/admin/admin_change_password.html", context)
    
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'> You are not Authorized for this page </h1>")