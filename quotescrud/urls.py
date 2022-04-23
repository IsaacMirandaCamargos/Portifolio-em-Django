from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.quotes_crud_list, name='quotes_crud_list'),
    path('delete/', views.quotes_crud_delete, name='quotes_crud_delete'),
    path('edit/', views.quotes_crud_edit, name='quotes_crud_edit'),
    path('create/', views.quotes_crud_create, name='quotes_crud_create'),
]