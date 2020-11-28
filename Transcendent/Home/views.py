from django.shortcuts import render
from WeeklyBulletin.views import Articles
from events.views import Events
from newsletter.views import Newsletter
import datetime

# Create your views here.

def home(request):

    def previous_week_range(date):
        end_date = date + datetime.timedelta(-date.weekday()-1)
        return end_date
    a=Articles.objects.exclude(date= previous_week_range(datetime.date.today()))
    
    return render(request,"homepage.html",{'articles': a,'events': Events.objects.all()})
def bulletin(request):
    return render(request,"bulletin.html",{'articles': Articles.objects.all()})
def events(request):
    return render(request,"events.html",{'events': Events.objects.all()})
def newspage(request):
    return render(request,"newsletter.html",{'newsletter': Newsletter.objects.all()})
