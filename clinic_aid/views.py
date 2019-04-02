from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, "index.html")

def articles(request, year):
    return HttpResponse("You was born in: " + str(year))