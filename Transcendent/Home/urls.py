from django.urls import path
from . import views

urlpatterns= [
    path('', views.home,name="home"),
    path('weeklybulletin/',views.bulletin,name="bulletin"),
    path('events&registrations/',views.events,name="events"),
    path('newspage/',views.newspage,name="newspage"),
    
    ]