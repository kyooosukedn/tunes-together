from django.shortcuts import render
from rest_framework import generics

from api.models import Room
from .serializers import RoomSerializer

# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

