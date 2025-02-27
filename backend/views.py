from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer
from .models import Message

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