from django.urls import path, include
from . import views


urlpatterns = [
    path('machine_learn/', views.machine_learn, name='machine_learn'),
]