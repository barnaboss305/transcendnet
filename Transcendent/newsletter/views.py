from django.shortcuts import render
from .models import Newsletter
# Create your views here.

def newspage(request):
    return render(request,"newsletter.html")

def newsletter(request):
    return render(request,"newsletter_page.html")