from django.shortcuts import render

from .models import Village, Villager

def index(request):
    """The home page for the Village Simulator site"""
    return render(request, 'villages/index.html')