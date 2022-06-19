from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Category, Item
from .serializers import (
    CategorySerializer,
    ItemSerializer
)
# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

class ItemViewset(viewsets.ModelViewSet):
    queryset=Item.objects.select_related('category')
    serializer_class=ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__id']
    search_fields = ['category']