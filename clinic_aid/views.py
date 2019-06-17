from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from clinic.models import Patient, Doctor, Appointment, Secretary, Time, Day
from django.views import View
from clinic.extras import check_date
import datetime

def hello(request):
    user = request.user
    if(user.is_authenticated):
        if(request.user.role == "medic"):
            return redirect("search")
        elif(user.role == "secretary"):
            return redirect("search")
    return render(request, "error_message.html")


class Search(View):

    results = None
    template_name = 'search.html'
    error = None

    @method_decorator(login_required)
    def get(self, request):
        if request.GET.get('name') is not None:
            if request.GET.get('type_search') == 'name_check':
                name = request.GET.get('name')
                self.results = Patient.objects.filter(name__startswith=name)
            elif request.GET.get('type_search') == 'cpf_check':
                pass
            else:
                return render(request, 'error_message.html')
            # self.results = CustomUser.objects.all()
        return render(request, self.template_name, {'results': self.results,
                                                    'error': self.error})


class PatientPage(View):

    def get(self, request, *args, **kwargs):

        result = Patient.objects.filter(id=kwargs['id'])[0]
        appts = Appointment.objects.filter(patient=result)

        return render(request, 'patient_page.html', {'result': result,
                                                     'appts': appts})


class DocSelection(View):
    results = None
    doctors = Doctor.objects.all()

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        error = ""
        return render(request, 'doc_selection.html', {'results': self.results, 'error': error,
                                                      'doctors': self.doctors})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if check_date(request.POST.get('date')):
            request.session['doctor'] = request.POST.get('doctor')
            request.session['date'] = request.POST.get('date')
            request.session['patient_id'] = self.kwargs['person']
            return redirect('info_appt')
        else:
            error = "Data deve ser maior que o dia atual!"

        return render(request, 'doc_selection.html', {'results': self.results, 'error': error,
                                                      'doctors': self.doctors})


# ControleAgendar
class ScheduleControl(View):
    results = None

    @method_decorator(login_required)
    def get(self, request):
        doctor_id = request.session.get('doctor')
        date = request.session.get('date')
        # patient_id = request.session.get('patient_id')

        doctor = Doctor.objects.filter(id=doctor_id)[0]
        # patient = Patient.objects.filter(id=patient_id)[0]

        date_doctor = doctor.day_set.filter(date=date)

        used_times = []
        if date_doctor:
            date_doctor = date_doctor[0]
            times_list = list(date_doctor.time_set.all())
            for time in times_list:
                used_times.append(time.time)

        print(used_times)
        times = []
        for i in range(9, 18):
            if str(i * 100) not in used_times:
                times.append(str(i) + ":00")
            if str(i * 100 + 30) not in used_times:
                times.append(str(i) + ":30")

        return render(request, 'info_appt.html', {'times': times})

    def post(self, request):

        a_hour = request.POST.get('select_horarios')
        a_reason = request.POST.get('reason_appt')
        a_obs = request.POST.get('observations')
        a_date = request.session.get('date')

        doctor_id = request.session.get('doctor')
        patient_id = request.session.get('patient_id')
        a_doctor = Doctor.objects.filter(id=doctor_id)[0]

        try:
            day = Day.objects.get(date=a_date)
        except Day.DoesNotExist:
            day = Day(date=a_date, doctor=a_doctor)
            day.save()
            day = Day.objects.get(date=a_date)

        a_patient = Patient.objects.filter(id=patient_id)[0]
        a_secretary = Secretary.objects.filter(user_x=request.user)[0]

        time = Time(time=a_hour.replace(':', ''), days=day)
        time.save()

        appt = Appointment(doctor=a_doctor, patient=a_patient, secretary=a_secretary,
                           reason=a_reason, hour=a_hour, observations=a_obs, date=day,
                           date_string=a_date)
        appt.save()

        return redirect('hello')


class RegisterPatient(View):

    def get(self, request):
        return render(request, 'register_patient.html')

    def post(self, request):
        f_date = request.POST.get('patient_date')
        f_gender = request.POST.get('patient_gender')
        f_cpf = request.POST.get('patient_cpf')
        f_name = request.POST.get('patient_name')
        f_plan = request.POST.get('patient_plan')
        f_nplan = request.POST.get('patient_plan_number')
        f_obs = request.POST.get('patient_observations')
        patient = Patient(name=f_name, dob=f_date, gender=f_gender, cpf=f_cpf,
                          plan=f_plan, number=f_nplan, observations=f_obs)
        patient.save()
        return redirect('hello')


class SearchAppt(View):
    error = None

    def get(self, request):
        request.session['active'] = 'no'
        name = request.GET.get('name')
        type_search = request.GET.get('type_search')
        appts = Appointment.objects.none()
        if name is not None:
            date_start = request.GET.get('date_start')
            date_end = request.GET.get('date_end')

            if type_search == 'patient_check':
                patients = Patient.objects.filter(name__startswith=name)
                for patient in patients:
                    appt = Appointment.objects.filter(patient=patient)
                    appts = appts | appt

            else:
                doctors = Doctor.objects.filter(name__startswith=name)
                for doc in doctors:
                    appt = Appointment.objects.filter(doctor=doc)
                    appts = appts | appt

            if date_start != '':
                appts = appts.filter(date_string__range=[date_start, date_end])

            if not appts:
                self.error = "a"

        return render(request, 'search_appt.html', {'error': self.error,
                                                    'appts': appts},)


def filter_date(query, start, end):
    start = start.split('-')
    end = end.split('-')
    start = datetime.datetime(int(start[0]), int(start[1]), int(start[2]))
    end = datetime.datetime(int(end[0]), int(end[1]), int(end[2]))

    print(query[0].date > start)

    for res in query:
        pass



class ApptPage(View):

    def get(self, request, *args, **kwargs):

        appt_id = self.kwargs['id']
        appt = Appointment.objects.get(id=appt_id)

        return render(request, 'appt_page.html', {'appt': appt})


class SeeAppt(View):

    def get(self, request):
        return render(request, 'see_appt.html')

    def post(self, request):
        request.session['active'] = 'yes'
        return redirect('appt_page')


class RegisterReturn(View):
    times_ok = None
    date = None

    def get(self, request):
        used_times = []
        times = []
        date = ''
        if request.GET.get('date'):
            if check_date(request.GET.get('date')):
                request.session['date'] = request.GET.get('date')
                for i in range(9, 18):
                    if i * 100 not in used_times:
                        times.append(str(i) + ":00")
                    if i * 100 + 30 not in used_times:
                        times.append(str(i) + ":30")
                date_split = request.GET.get('date').split('-')
                date = date_split[2] + '/' + date_split[1] + '/' + date_split[0]
                self.times_ok = True
            else:
                print("data n ok")

        return render(request, 'register_return.html',
                      {'times_ok': self.times_ok, 'times': times,
                       'date': date})

    def post(self, request):
        print(str(request.session.get('date')) + ' ' +
              str(request.POST.get('select_horarios')))
        return redirect('hello')


def confirm(request):
    return render(request, 'confirm_see.html')
