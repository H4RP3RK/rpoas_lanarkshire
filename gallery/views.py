from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Image


def view_gallery(request):
    """ view for gallery page """
    images = Image.objects.order_by('location')
    query = None
    locations = None
    filterLocation = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            """ search by keyword in title or caption"""
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a search term into the search box.')
                return redirect(reverse('gallery'))
            
            queries = Q(title__icontains=query) | Q(caption__icontains=query)
            images = images.filter(queries)
        
        if 'location' in request.GET:
            filterLocation = request.GET['location'].split(',')
            images = images.filter(location__in=filterLocation)
            filterLocation = Image.objects.filter(location__in=images)
        
        # if 'year' in request.GET:
        #     filterYear = request.GET['year'].split(',')
        #     images = images.filter(year__in=filterYear)
        #     filterYear = Image.objects.filter(year__in=images)
        
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'location':
                sortkey = 'lower_location'
                images = images.annotate(lower_location=Lower('location'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            images = images.order_by(sortkey)
        
    current_sorting = f'{sort}_{direction}'

    context = {
        'images': images,
        'search_term': query,
        'current_location': locations,
        'current_sorting': current_sorting,
    }

    return render(request, 'gallery/gallery.html', context)
