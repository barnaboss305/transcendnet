from django.shortcuts import render
from .models import Events
# Create your views here.


def events(request):
    return render(request,"events.html")