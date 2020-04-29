from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Meeting, Room


def details(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/room_details.html', {'rooms': rooms})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {'form': form})
