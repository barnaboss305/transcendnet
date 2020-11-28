from django.shortcuts import render
from .models import Articles

def bulletin(request):
    articles=Articles.objects.all()
    return render(request,"bulletin.html",{'articles':Articles.objects.all()})

def article(request):
    a_id=request.GET['id']
    article=Articles.objects.get(pk=a_id)
    return render(request,"article.html",{'article':article})