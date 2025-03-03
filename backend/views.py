from rest_framework import status #type: ignore
from rest_framework.decorators import api_view #type: ignore
from rest_framework.response import Response #type: ignore
from .serializers import MessageSerializer, RoomSerializer
from .models import Message, Room

# Create your views here.
@api_view(['GET', 'POST'])
def Messages(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response({'data': serializer.data})
    
    elif request.method == 'POST':
        data = request.data
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({'data': serializer.data})

@api_view(['GET', 'POST'])    
def Rooms(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({'data': serializer.data})
    
    elif request.method == 'POST':
        data = request.data
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({'data': serializer.data})