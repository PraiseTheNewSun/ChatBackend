from rest_framework import serializers #type:ignore
from .models import Message, Room

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'body', 'date']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_name', 'room_pass']