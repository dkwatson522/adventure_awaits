from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('guide/<str:pk>/', views.guide, name='guide'),
]
