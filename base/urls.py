from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('error', views.errorPage, name='error'),
    path('', views.home, name='home'),
    path('guide/<str:pk>/', views.guide, name='guide'),
    path('create-guide', views.createGuide, name ='create-guide'),
    path('update-guide/<str:pk>/', views.updateGuide, name='update-guide'),
    path('delete-guide/<str:pk>/', views.deleteGuide, name='delete-guide'),
]
