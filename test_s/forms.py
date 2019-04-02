from django import forms
from .models import Person

class PersonForm(forms.ModelForm):

    first_name = forms.CharField(
        label='nameee',
        max_length=1000,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'csstest'}
        )
    )

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary']
