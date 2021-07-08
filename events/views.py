from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Event
from .serializers import EventSerializer


class EventsViewset(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer

    # def get_queryset(self):
    #     qs=self.queryset
    #     for i in qs:
    #         print(i.start.strftime("%Y-%m-%d %H:%M"))
           

    #         return qs

            # YYYY-MM-DD