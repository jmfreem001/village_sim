"""Defines url patters for villages"""

from django.urls import path

from . import views

app_name = 'villages'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]