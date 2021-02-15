from django.shortcuts import render
from .models import Event


def events(request):
    """ view for events page """
    events = Event.objects.order_by('datetime')
    context = {
        'events': events,
    }
    return render(request, 'events/events.html', context)
