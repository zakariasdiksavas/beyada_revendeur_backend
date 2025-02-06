from django.urls import path
from . import views

urlpatterns = [
    path('create-achat', views.create_achat),
    path('update-achat', views.update_achat),
    path('delete-achat', views.delete_achat),
    path('list-achat', views.list_achat),
]