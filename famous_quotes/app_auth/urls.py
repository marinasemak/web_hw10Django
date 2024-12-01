from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from . import views
from .forms import LoginForm

app_name = "app_auth"

urlpatterns = [
    path("signup/", views.RegisterView.as_view(), name="signup"),
    path(
        "signin/",
        LoginView.as_view(
            template_name="app_auth/login.html",
            form_class=LoginForm,
            redirect_authenticated_user=True,
        ),
        name="signin",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_reset/", views.ResetPasswordView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(
            template_name="app_auth/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="app_auth/password_reset_confirm.html",
            success_url="/auth/password_reset/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="app_auth/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
