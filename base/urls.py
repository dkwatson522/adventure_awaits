from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guide/<str:pk>/', views.guide, name='guide'),
    path('create-guide', views.createGuide, name ='create-guide'),
    path('update-guide/<str:pk>/', views.updateGuide, name='update-guide'),
    path('delete-guide/<str:pk>/', views.deleteGuide, name='delete-guide'),
]
