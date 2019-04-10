from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    role = forms.CharField(
        label='roleee',
        max_length=1000,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'csstest'}
        )
    )

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'role',]

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'role',]
