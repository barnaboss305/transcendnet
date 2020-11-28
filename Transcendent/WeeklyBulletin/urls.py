from django.urls import path
from . import views

urlpatterns= [
    path('', views.bulletin,name="bulletin"),
    path('article',views.article,name="article"),
    ]