from django.shortcuts import render


def index(request):
    """ view for home page """
    return render(request, 'home/index.html')

def mailchimp_signup(request):
    """ view for mailchimp signup page """
    return render(request, 'home/mailchimp_signup.html')
