from django.urls import path
from . import views

urlpatterns= [
    path('', views.newspage,name="newspage"),
    path('newsletter',views.newsletter,name="newsletter"),
    ]