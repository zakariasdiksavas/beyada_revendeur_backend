from rest_framework import serializers
from .models import Paiment, PaiementProof




class PaiementProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaiementProof
        fields = '__all__'
class PaimentVenteSerializer(serializers.ModelSerializer):
    paiment = PaiementProofSerializer(many=True, read_only=True)
    class Meta:
        model = Paiment
        fields = ("id", "client_vente", "vente", "montant", "date", "status", "paiement_mode", "paiment")

class PaimentClientSerializer(serializers.ModelSerializer):
    paiment = PaiementProofSerializer(many=True, read_only=True)
    class Meta:
        model = Paiment
        fields = ["id", "client_client", "montant", "date", "status", "paiement_mode", "paiment"]


