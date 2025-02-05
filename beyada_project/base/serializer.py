from rest_framework import serializers
from .models import Fournisseur, Site, Batiment, Client


class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = ("id", "name", "address", "phone","email", "user")

class SiteSerializer(serializers.ModelSerializer):
    fournisseur_name = serializers.CharField(source="fournisseur.name", read_only=True)
    class Meta:
        model = Site
        fields = ("id", "name", "address", "phone","fournisseur", "fournisseur_name")

class BatimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batiment
        fields = ("id", "site", "name")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "name", "user", "address", "phone", "email", "is_passager", "is_active")



class ClientSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "name")