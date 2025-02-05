from django.urls import path
from . import views

urlpatterns = [
    path('create-fournisseur', views.create_fournisseur),
    path('update-fournisseur', views.update_fournisseur),
    path('delete-fournisseur', views.delete_fournisseur),
    path('list-fournisseur', views.list_fournisseur),

    path('create-site', views.create_site),
    path('update-site', views.update_site),
    path('delete-site', views.delete_site),
    path('list-site', views.list_site),

    path('create-batiment', views.create_batiment),
    path('update-batiment', views.update_batiment),
    path('delete-batiment', views.delete_batiment),
    path('list-batiment', views.list_batiment),

    path('create-client', views.create_client),
    path('update-client', views.update_client),
    path('delete-client', views.delete_client),
    path('list-client', views.list_client),


    path('list-select-data', views.get_select_data),
    path('list-select-client', views.get_select_client),

]