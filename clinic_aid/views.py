from django.http import HttpResponse
from django.shortcuts import render
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
def articles(request, year):
    return HttpResponse("You was born in: " + str(year))

@login_required
def search(request):
    results = None
    print(str(request.GET.get('name')))
    if(request.GET.get('name') != None):
        results = CustomUser.objects.all()
    return render(request, 'search.html', {'results':results})
