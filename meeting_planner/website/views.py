import datetime

from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import *


def welcome(request):
    context = {'meetings': Meeting.objects.all()}
    return render(request, "website/welcome.html", context)


def date(request):
    return HttpResponse(f"This page was served at {datetime.datetime.now()}")


def about(request):
    return HttpResponse("Hello I am Shubham Singh, Just trying out Dajngo 3.0")
