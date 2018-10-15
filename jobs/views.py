from django.shortcuts import render

from .models import Job


def home(request):
    #get the objects from database below, awesome!!
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
