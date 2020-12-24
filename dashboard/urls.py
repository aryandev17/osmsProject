from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_user, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path("submit_request/", views.submit_request, name="submit_request"),
    path("service_status/", views.service_status, name="service_status"),
    path("change_password/", views.change_password, name="change_password"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard")
]
