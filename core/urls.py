from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_criminal, name='add_criminal'),
    path('personalize_memory/<int:criminal_id>/', views.personalize_memory, name='personalize_memory'),
    path('simulation_result/<int:criminal_id>/', views.simulation_result, name='simulation_result'),
]