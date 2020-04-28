import datetime

from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to meeting planner")


def date(request):
    return HttpResponse(f"This page was served at {datetime.datetime.now()}")


def about(request):
    return HttpResponse("Hello I am Shubham Singh, Just trying out Dajngo 3.0")
