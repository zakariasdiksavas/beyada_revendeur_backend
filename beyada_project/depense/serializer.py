from rest_framework import serializers
from .models import *

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = "__all__"


class MainDoeuvreSerializer(serializers.ModelSerializer):
    personnel_name = serializers.CharField(source="personnel.name", read_only=True)
    class Meta:
        model = MainDoeuvre
        fields = "__all__"

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class DiversSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta:
        model = Divers
        fields = "__all__"
