from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    usename = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'username',
                'id': 'username',
                'placeholder': 'Username',
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailField(
            attrs={
                'class': 'email',
                'id': 'email',
                'placeholder': 'Email',
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'pass1',
                'id': 'pass1',
                'placeholder': 'Enter Password'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'pass2',
                'id': 'pass2',
                'placeholder': 'Re-Enter Password',
            }
        )
    )


    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
        ]


class Authenticate(AuthenticationForm):
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'pass',
                'id': 'pass',
                'placeholder': 'Enter Password',
            }
        )
    )

    usename = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'username',
                'id': 'username',
                'placeholder': 'Username',
            }
        )
    )
