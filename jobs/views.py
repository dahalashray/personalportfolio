from django.shortcuts import render
from .models import Job

def home(request):
    return render(request, 'jobs/home.html')

