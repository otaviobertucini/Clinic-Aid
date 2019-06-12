from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CustomUser, Secretary

# class SignUp(View):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'new_user.html'

class SignUp(generic.CreateView):

    def get(self, request):
        form = CustomUserCreationForm
        return render(request, 'new_user.html', {'form': form})

    def post(self, request):

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')



