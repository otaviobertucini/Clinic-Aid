from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from clinic.models import CustomUser

def hello(request):
    user = request.user
    if(user.is_authenticated):
        if(request.user.role == "medic"):
            return render(request, "home_doctor.html")
        elif(user.role == "secretary"):
            return render(request, "home_secretary.html")
    return render(request, "error_message.html")

@login_required
def search(request):
    results = None
    if(request.GET.get('name') != None):
        if(request.GET.get('type_search') == 'name_check'):
            pass
        elif(request.GET.get('type_search') == 'cpf_check'):
            pass
        else:
            return render(request, 'error_message.html')
        results = CustomUser.objects.all()
    return render(request, 'search.html', {'results':results})

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
