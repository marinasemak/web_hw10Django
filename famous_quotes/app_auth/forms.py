from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, EmailField, TextInput, EmailInput, PasswordInput


class RegistrationForm(UserCreationForm):
    username = CharField(
        max_length=100, required=True, widget=TextInput(attrs={"class": "form-control"})
    )

    email = EmailField(
        max_length=100,
        required=True,
        widget=EmailInput(attrs={"class": "form-control"}),
    )

    password1 = CharField(
        max_length=50,
        required=True,
        widget=PasswordInput(attrs={"class": "form-control"}),
    )

    password2 = CharField(
        max_length=50,
        required=True,
        widget=PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = CharField(
        max_length=100, required=True, widget=TextInput(attrs={"class": "form-control"})
    )

    password = CharField(
        max_length=50,
        required=True,
        widget=PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ["username", "password"]
