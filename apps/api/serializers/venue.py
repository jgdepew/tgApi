from rest_framework import serializers
from apps.api.models import Venue


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'about', 'created_at', 'updated_at')

class VenueSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'created_at', 'updated_at')