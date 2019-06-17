"""clinic_aid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import hello
from .views import Search, DocSelection, ScheduleControl, RegisterPatient, \
    SearchAppt, ApptPage, SeeAppt, RegisterReturn, PatientPage, CancelAppt, Confirm
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from clinic import views as clinic_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', clinic_views.SignUp.as_view(), name='register'),
    path('hello/', hello, name="hello"),
    path('admin/', admin.site.urls),
    path('search/', Search.as_view(), name="search"),
    path('patient/<int:id>', PatientPage.as_view(), name='patient_page'),
    path('doc_selection/<str:person>', DocSelection.as_view(), name='doc_selection'),
    path('info_appt', ScheduleControl.as_view(), name='info_appt'),
    path('new_paciente', RegisterPatient.as_view(), name='new_patient'),
    path('search_appt', SearchAppt.as_view(), name="search_appt"),
    path('see_appt/<int:id>', SeeAppt.as_view(), name="see_appt"),
    path('reg_return/<int:id>', RegisterReturn.as_view(), name="reg_return"),
    path('confirm', Confirm.as_view(), name="confirm"),
    path('appt_page/<int:id>', ApptPage.as_view(), name="appt_page"),
    path('cancel/<int:id>', CancelAppt.as_view(), name="cancel_appt"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
