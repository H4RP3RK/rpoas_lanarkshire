from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Image


def view_gallery(request):
    """ view for gallery page """
    images = Image.objects.all()
    locations = None
    filterLocation = None
    query = None

    if request.GET:
        if 'q' in request.GET:
            """ search by keyword in title or caption"""
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a search term into the search box.')
                return redirect(reverse('gallery'))
            
            queries = Q(title__icontains=query) | Q(caption__icontains=query)
            images = images.filter(queries)
        

        # if 'location' in request.GET:
        #     """ filter by location """
        #     filterLocation = request.GET['location'].split(',')
        #     images = images.filter(image__location__in=filterLocation)



    context = {
        'images': images,
    }

    return render(request, 'gallery/gallery.html', context)
