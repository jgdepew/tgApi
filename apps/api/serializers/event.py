from rest_framework import serializers
from apps.api.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'entertainer', 'venue', 'date', 'type', 'created_at', 'updated_at')

class EventSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'entertainer', 'venue', 'date', 'created_at', 'updated_at')