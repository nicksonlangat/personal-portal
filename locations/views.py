from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import County, Constituency, Ward
from .serializers import (
    CountySerializer,
    ConstituencySerializer,
    WardSerializer
)
# Create your views here.
class CountyViewset(viewsets.ModelViewSet):
    queryset=County.objects.all()
    serializer_class=CountySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

class CostituencyViewset(viewsets.ModelViewSet):
    queryset=Constituency.objects.select_related('county')
    serializer_class=ConstituencySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'county__id']
    search_fields = ['name']

class WardViewset(viewsets.ModelViewSet):
    queryset=Ward.objects.select_related('constituency')
    serializer_class=WardSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'constituency__id']
    search_fields = ['name']