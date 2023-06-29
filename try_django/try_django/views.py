from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {'title': 'home'}
    return render(request, "home.html", context)

def contact_page(request):
    context = {'title': 'Contact'}
    return render(request, "contact.html", context)

def about_page(request):
    context = {'title': 'About Us'}
    return render(request, "about.html", context)
