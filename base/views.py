from django.shortcuts import render
from .models import Guide

def home(request):
  guides = Guide.objects.all()
  context = {'guides': guides}
  return render(request, 'base/home.html', context)

def guide(request, pk):
  guide = Guide.objects.get(id=pk)

  context = {'guide': guide}
  return render(request, 'base/guide.html', context)
