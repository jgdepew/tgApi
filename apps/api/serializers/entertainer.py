from rest_framework import serializers
from apps.api.models import Entertainer

class EntertainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainer
        fields = ('id', 'name', 'about', 'type', 'created_at', 'updated_at')

class EntertainerSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Entertainer
        fields = ('id', 'name', 'about', 'created_at', 'updated_at')