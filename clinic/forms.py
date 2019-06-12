from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    role = forms.ChoiceField(choices=[("medic", "Medic"), ("secretary", "Secretary")],
                             required=True)
    name = forms.CharField(max_length=100, required=True)
    dob = forms.DateField(required=True)
    gender = forms.ChoiceField(choices=[("m", "Masculino"), ("f", "Feminino")],
                             required=True)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'role', 'name', 'dob', 'gender']

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
