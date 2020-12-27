from django.shortcuts import render
from .models import Event


def events(request):
    """ view for events page """
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'events/events.html', context)
