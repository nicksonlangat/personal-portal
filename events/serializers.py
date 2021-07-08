from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Event
        fields=[
            'id',
            'name',
            'details',
            'start',
            'end',
            'color'
        ]