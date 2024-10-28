# Serializers for Recipes API
from rest_framework import serializers

from core.models import (
    Bird,
)

class BirdSerializer(serializers.ModelSerializer):
    """Serializer for birds."""

    class Meta:
        model = Bird
        fields = ['id', 'name', 'sciName', 'region', 'family', 'order', 'status']
        read_only_fields = ['id']