from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'you@example.com'
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email