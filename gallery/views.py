from django.shortcuts import render


def view_gallery(request):
    """ view for gallery page """
    return render(request, 'gallery/gallery.html')
