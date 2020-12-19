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
