from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserExt

class UserExtSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExt
        fields = ['user', 'phone', 'fournisseur']
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}