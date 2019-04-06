from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def hello(request):
    return render(request, "index.html")

@login_required
def articles(request, year):
    return HttpResponse("You was born in: " + str(year))
