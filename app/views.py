from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from . import forms
# from .models import InternshipPost, OpenSourcePost

# Create your views here.
def index_handler(request):
    context = {
        # 'internshipPosts' : InternshipPost.objects.all()[0:3],
        # 'openSourcePosts' : OpenSourcePost.objects.all()[0:3]
    }
    return render(request, 'index.html', context)

def register_handler(request):
    return render(request, 'register.html')

class Register (CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name='register.html'

def dashboard_handler(request):
    return render(request, 'dashboard.html')        
