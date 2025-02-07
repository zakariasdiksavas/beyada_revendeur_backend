from django.urls import path
from . import views

urlpatterns = [
    path('create-paiment-vente', views.create_paimentVente),
    path('update-paiment-vente', views.update_paimentVente),
    path('delete-paiment-vente', views.delete_paimentVente),
    path('list-paiment-vente', views.list_paimentVente),
    path('update-status-paiment-vente', views.update_paiment_status_vente),
        
    path('create-paiment-client', views.create_paimentClient),
    path('update-paiment-client', views.update_paimentClient),
    path('delete-paiment-client', views.delete_paimentClient),
    path('list-paiment-client', views.list_paimentClient),
    path('update-status-paiment-client', views.update_paiment_status_client),

    path('add-paiement-proof', views.add_payment_try_proof),
    path('update-paiement-proof', views.update_payment_try_proof),
    path('delete-paiement-proof', views.delete_payment_try_proof),
    
]