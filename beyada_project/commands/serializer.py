from rest_framework import serializers

from .models import *
class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = "__all__"