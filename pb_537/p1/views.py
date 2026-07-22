from django.shortcuts import render
from .models import Event
# Create your views here.
from .serializers import EventSerializer
from .permission import IsA
from rest_framework import viewsets
class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[IsA]