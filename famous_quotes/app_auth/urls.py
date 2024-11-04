from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = "app_auth"

urlpatterns = [
    path("signup/", LoginView.as_view(), name="signup"),
    path("signin/", LoginView.as_view(), name="signin"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
