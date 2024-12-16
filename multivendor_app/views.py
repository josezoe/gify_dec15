# multivendor_app/views.py
from django.shortcuts import render
def home(request):
    return render(request, 'home.html') #Create a home.html in templates folder