from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Image


def view_gallery(request):
    """ view for gallery page """
    images = Image.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a search term into the search box.')
                return redirect(reverse('gallery'))
            
            queries = Q(title__icontains=query) | Q(caption__icontains=query)
            images = images.filter(queries)

    context = {
        'images': images,
    }
    
    return render(request, 'gallery/gallery.html', context)
