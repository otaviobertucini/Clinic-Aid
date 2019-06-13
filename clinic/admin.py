from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Patient, Secretary, Doctor, Day, Time, Appointment


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['role', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Secretary)
admin.site.register(Doctor)
admin.site.register(Day)
admin.site.register(Time)
admin.site.register(Appointment)
