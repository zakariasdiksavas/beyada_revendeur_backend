from rest_framework import serializers
from .models import Achats

class AchatSerializer(serializers.ModelSerializer):
    batiment_name = serializers.CharField(source='batiment.name', read_only=True)
    site_name = serializers.CharField(source='batiment.site.name', read_only=True)

    class Meta:
        model = Achats
        fields = ('id', 'batiment', 'batiment_name', 'site_name', 'quantity', 'poids_plateau', 'pu', 'date', 'classe')