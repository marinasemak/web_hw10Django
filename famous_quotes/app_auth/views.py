from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView

# Create your views here.


class RegisterView(View):
    template_name = "app_auth/registration.html"
    form_class = RegistrationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(
                request, f"Hello {username}. Your account successfully created."
            )
            return redirect(to="app_auth:signin")
        return render(request, self.template_name, {"form": form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "app_auth/password_reset.html"
    email_template_name = "app_auth/password_reset_email.html"
    html_email_template_name = "app_auth/password_reset_email.html"
    success_url = reverse_lazy("app_auth:password_reset_done")
    success_message = (
        "An email with instructions to reset your password has been sent to %(email)s."
    )
    subject_template_name = "app_auth/password_reset_subject.txt"
