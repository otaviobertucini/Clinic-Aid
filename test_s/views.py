from django.shortcuts import render
from .forms import PersonForm

def new_person(request):
    form = PersonForm(request.POST, None)
    return render(request, 'new.html', {'form':form})

