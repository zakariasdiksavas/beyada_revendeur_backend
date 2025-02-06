from rest_framework import serializers
from .models import PaimentByVente

class PaimentVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaimentByVente
        fields = ("id", "client_vente", "vente", "montant", "date", "status", "paiement_mode")