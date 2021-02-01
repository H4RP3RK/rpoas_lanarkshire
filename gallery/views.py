from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q, Count
from django.db.models.functions import Lower
from .models import Image


def view_gallery(request):
    """ view for gallery page """
    images = Image.objects.order_by()
    locationValues = images.order_by('location').values('location').distinct()
    yearValues = images.order_by('year').values('year').distinct()
    query = None
    locations = None
    filterLocation = None
    filterYear = None
    sort = None
    direction = None

    if request.GET:
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

        if 'location' in request.GET:
            filterLocation = request.GET['location'].split(',')
            filterLocationValue = filterLocation[0]
            images = images.filter(location__in=filterLocation)
            locationValues = images.values('location').distinct()
            yearValues = images.values('year').distinct()
            if 'sort' in request.GET:
                images = images.order_by(sortkey)
        
        if 'year' in request.GET:
            filterYear = request.GET['year'].split(',')
            filterYearValue = filterYear[0]
            images = images.filter(year__in=filterYear)
            yearValues = images.values('year').distinct()
            locationValues = images.values('location').distinct()

        if 'q' in request.GET:
            """ search by keyword in title or caption"""
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a search term into the search box.')
                return redirect(reverse('gallery'))
            
            queries = Q(title__icontains=query) | Q(caption__icontains=query)
            images = images.filter(queries)
            yearValues = images.values('year').distinct()
            locationValues = images.values('location').distinct()
        
    current_sorting = f'{sort}_{direction}'

    context = {
        'images': images,
        'image_count': images.count(),
        'search_term': query,
        'current_location': locations,
        'current_sorting': current_sorting,
        'location_values': locationValues,
        'year_values': yearValues
    }

    return render(request, 'gallery/gallery.html', context)
