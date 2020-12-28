from django.shortcuts import render


def contact(request):
    """ view for contact page """
    return render(request, 'contact/contact.html')
