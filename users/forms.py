from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
)
from django.contrib.auth.models import User


class UserCreationFormWithEmail(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "my-4",
            }
        ),
        label="",
    )

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "my-4",
            },
        ),
        label="",
    )

    password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "my-4",
            }
        ),
        label="",
    )

    password2 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "my-4",
            }
        ),
        label="",
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "my-4",
            }
        ),
        label="",
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "my-4",
            }
        ),
        label="",
    )

    class Meta:
        model = User
        fields = ["username", "password"]
