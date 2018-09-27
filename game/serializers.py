from rest_framework import serializers
from game.models import *

class ProcessSerializer(serializers.ModelSerializer):
    """Serializer to map the Vmd model instance into json format."""

    class Meta:
        """Map serializer to model Vmd and their fields."""
        model = Process
        fields = '__all__'
