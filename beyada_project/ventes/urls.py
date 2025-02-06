from django.urls import path
from . import views

urlpatterns = [
    path('create-vente', views.create_vente),
    path('update-vente', views.update_vente),
    path('delete-vente', views.delete_vente),
    path('list-vente', views.list_vente),


]