from django.shortcuts import render


def events(request):
    """ view for events page """
    return render(request, 'events/events.html')
