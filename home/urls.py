from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/mailchimp_signup/', views.mailchimp_signup, name='mailchimp_signup'),
]