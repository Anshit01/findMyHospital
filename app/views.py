from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from . import forms
from .models import Hospital

# Create your views here.
def index_handler(request):
    context = {}
    if request.method == 'GET' and request.GET:
        location = request.GET['location']
        # bg = request.GET['bg']
        if location != '':
            context = {
                'hospitals' : Hospital.objects.all().filter(location=location, show=True),
                'location' : location
            }
        return render(request, 'index.html', context)
    context = {
        'hospitals' : Hospital.objects.filter(show=True)
    }
    return render(request, 'index.html', context)

def hospital_handler(request, id):
    context = {
        'hospital' : Hospital.objects.filter(id=id)[0]
    }
    return render(request, 'hospital_detail.html', context)

def register_handler(request):
    return render(request, 'register.html')

class Register (CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name='register.html'

def dashboard_handler(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Hospital.objects.create(
                
            )
        else:
            context = {}
            hospitals = Hospital.objects.filter(email=request.user.email)
            if len(hospitals) == 0:
                context['flag'] = False
            else:
                context['flag'] = True
                context['hospital'] = hospitals[0]
            return render(request, 'dashboard.html', context)
    return redirect('/')       
