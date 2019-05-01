from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from clinic.models import CustomUser
from django.views import View


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


@login_required
def doc_selection(request):
    results = None
    if (request.GET.get('doctor') != None):
        results = CustomUser.objects.all()
        request.session['doctor'] = request.GET.get('doctor')
        request.session['date'] = request.GET.get('date')

        return redirect('info_appt')

    return render(request, 'doc_selection.html', {'results':results})


@login_required
def info_appt(request):
    doctor = request.session.get('doctor')
    date = request.session.get('date')
    return render(request, 'info_appt.html', {'doctor':doctor, 'date':date})
