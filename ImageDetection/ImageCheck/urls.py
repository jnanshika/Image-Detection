from django.contrib import admin
from django.urls import path
from ImageCheck import views

urlpatterns = [
    path('', views.index, name='ImageDetection'),
]
