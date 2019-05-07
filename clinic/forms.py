from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    role = forms.ChoiceField(choices=[("medic", "Medic"), ("secretary", "Secretary")],
                             required=True)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'role',]

        widgets = {
            'role': forms.Select(attrs={'class': 'csstest'})
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'role',]

class DocSelecionForm(forms.Form):
    doctor = forms.CharField(label="Name", required=True)
    date = forms.DateField(required=True, )
