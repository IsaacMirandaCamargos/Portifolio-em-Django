from django.urls import path, include
from . import views


urlpatterns = [
    path('machine_learn_home/', views.machine_learn_home, name='machine_learn_home'),
    path('machine_learn_evaluating/', views.machine_learn_evaluating, name='machine_learn_evaluating')
]