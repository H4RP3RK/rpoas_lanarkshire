from django.shortcuts import render
from .models import Image


def view_gallery(request):
    """ view for gallery page """
    images = Image.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'gallery/gallery.html', context)
