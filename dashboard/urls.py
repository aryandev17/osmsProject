from django.urls import path
from . import views

urlpatterns = [
    path("user_profile/", views.user_profile, name="user_profile"),
    path("signup/", views.signup_user, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout")
]
