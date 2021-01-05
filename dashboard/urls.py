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
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin_requests/", views.admin_requests, name="admin_requests"),
    path("assigned_order/", views.assigned_order, name="assigned_order"),
    path("technician_list/", views.technician_list, name="technician_list"),
    path("delete_assigned_order/<int:request_id>", views.delete_assigned_order, name="delete_assigned_order"),
    path("view_assigned_order/<int:request_id>", views.view_assigned_order, name="view_assigned_order"),
    path("add_technician/<int:employee_id>", views.add_technician, name="add_technician"),
    path("delete_technician/<int:employee_id>", views.delete_technician, name="delete_technician"),
    path("work_report/", views.work_report, name="work_report"),
    path("admin_edit_profile/", views.admin_edit_profile, name="admin_edit_profile"),
    path("admin_change_password/", views.admin_change_password, name="admin_change_password")
]
