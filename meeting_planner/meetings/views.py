from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Meeting, Room


def details(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/room_details.html', {'rooms': rooms})
