from django.urls import path
from . import views

urlpatterns = [
    path('create-paiment-vente', views.create_paimentVente),
    path('update-paiment-vente', views.update_paimentVente),
    path('delete-paiment-vente', views.delete_paimentVente),
    path('list-paiment-vente', views.list_paimentVente),
    path('update-status-paiment', views.update_paiment_status),


]