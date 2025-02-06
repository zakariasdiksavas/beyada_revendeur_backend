from rest_framework import serializers
from .models import Ventes

class VenteSerializer(serializers.ModelSerializer):
    batiment_name = serializers.CharField(source='batiment.name', read_only=True)
    site_name = serializers.CharField(source='batiment.site.name', read_only=True)
    client_name = serializers.CharField(source='client.name', read_only=True)
    class Meta:
        model = Ventes
        fields = ('id', 'batiment', 'batiment_name', 'site_name', 'client_name', 'client', 'quantity', 'poids_plateau', 'pu', 'date', 'classe')