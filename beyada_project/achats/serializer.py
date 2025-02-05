from rest_framework import serializers
from .models import Achats

class AchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achats
        fields = ('id', 'batiment', 'quantity', 'poids_plateau', 'pu', 'date', 'classe')