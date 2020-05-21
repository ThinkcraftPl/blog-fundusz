from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('posty', views.home),
    path('generate', views.generate),
    path('generateend', views.generateend),
]