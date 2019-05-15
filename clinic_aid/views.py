from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from clinic.models import CustomUser
from django.views import View
from clinic.extras import check_date


appt_ative = 'no'


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
                if request.GET.get('name') == 'maria':
                    self.error = 'a'
                else:
                    self.error = None
            elif request.GET.get('type_search') == 'cpf_check':
                pass
            else:
                return render(request, 'error_message.html')
            self.results = CustomUser.objects.all()
        return render(request, self.template_name, {'results': self.results,
                                                    'error': self.error})


@login_required
def patient_page(request, id):
    return render(request, 'patient_page.html')


class DocSelection(View):
    results = None

    @method_decorator(login_required)
    def get(self, request):
        error = ""
        if request.GET.get('doctor') is not None:
            if check_date(request.GET.get('date')):
                request.session['doctor'] = request.GET.get('doctor')
                request.session['date'] = request.GET.get('date')
                return redirect('info_appt')
            else:
                error = "Data deve ser maior que o dia atual!"
        return render(request, 'doc_selection.html', {'results': self.results, 'error': error})


# ControleAgendar
class ScheduleControl(View):
    results = None

    @method_decorator(login_required)
    def get(self, request):
        doctor = request.session.get('doctor')
        date = request.session.get('date')
        # doctor = ''
        # date = ''
        used_times = []
        times = []
        for i in range(9, 18):
            if i * 100 not in used_times:
                times.append(str(i) + ":00")
            if i * 100 + 30 not in used_times:
                times.append(str(i) + ":30")

        return render(request, 'info_appt.html', {'times': times})

    def post(self, request):
        return redirect('hello')


class RegisterPatient(View):

    def get(self, request):
        return render(request, 'register_patient.html')

    def post(self, request):
        print("Paciente cadastrado!")
        return redirect('hello')


class SearchAppt(View):
    results = None
    error = None
    def get(self, request):
        request.session['active'] = 'no'
        if request.GET.get('name') is not None:
            if request.GET.get('name') == 'maria':
                self.error = 'b'
            else:
                self.error = None
            self.results = 'a'

        return render(request, 'search_appt.html', {'results': self.results,
                                                    'error': self.error})


class ApptPage(View):

    def get(self, request):
        print(str(request.session.get('active')))
        if(request.session.get('active') == 'yes'):
            active = True
        else:
            active = False

        return render(request, 'appt_page.html', {'active': active,
                                                  'active2': appt_ative})


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
