from rest_framework import serializers
from .models import SavedProduct, SavedEvent, SavedService

class SavedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedProduct
        fields = ['user', 'product', 'item_id', 'item_type']

class SavedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedEvent
        fields = ['user', 'event']

class SavedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedService
        fields = ['user', 'service']