from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'education_level',
            'preferred_institute',
            'career_interest',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name'
            }),

            'education_level': forms.Select(),

            'preferred_institute': forms.TextInput(attrs={
                'placeholder': 'Enter your preferred institute'
            }),

            'career_interest': forms.TextInput(attrs={
                'placeholder': 'e.g. Software Development'
            }),
        }