from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from clinic.models import CustomUser
from django.views import View
from clinic.extras import check_date


def hello(request):
    user = request.user
    if(user.is_authenticated):
        if(request.user.role == "medic"):
            return render(request, "home_doctor.html")
        elif(user.role == "secretary"):
            return render(request, "home_secretary.html")
    return render(request, "error_message.html")


class Search(View):

    results = None
    template_name = 'search.html'

    @method_decorator(login_required)
    def get(self, request):
        if request.GET.get('name') is not None:
            if request.GET.get('type_search') == 'name_check':
                pass
            elif request.GET.get('type_search') == 'cpf_check':
                pass
            else:
                return render(request, 'error_message.html')
            self.results = CustomUser.objects.all()
        return render(request, self.template_name, {'results':self.results})


@login_required
def pacient_page(request, id):
    return render(request, 'pacient_page.html')


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
