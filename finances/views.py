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
    queryset=Item.objects.select_related('category').order_by('-created_at')
    serializer_class=ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__id']
    search_fields = ['category']

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Sum
from datetime import datetime

class CombinedData(APIView):
    permission_classes = [AllowAny,]
    def get(self, request, format=None):
        # x = Item.objects.values('category').annotate(total=Sum('amount'))
        # print(x)
        currentMonth = datetime.now().month
        prevMonth = currentMonth - 1
        categories = Category.objects.all()
        current_data = []
        last_data = []
        all_data = []
        for category in categories:
            sum = Item.objects.filter(
                category=category, 
                created_at__month=currentMonth
                ).aggregate(Sum('amount'))['amount__sum']
            current_data.append(
                {
                    "category":category.name,
                    "sum":0 if sum is None else sum
                }
            )
            sum = Item.objects.filter(
                category=category, 
                created_at__month=prevMonth
                ).aggregate(Sum('amount'))['amount__sum']
            last_data.append(
                {
                    "category":category.name,
                    "sum":0 if sum is None else sum
                }
            )
            sum = Item.objects.filter(category=category).aggregate(Sum('amount'))['amount__sum']
            all_data.append(
                {
                    "category":category.name,
                    "sum":0 if sum is None else sum
                }
            )
        return Response({
            "current":current_data,
            "previous":last_data,
            "all":all_data
        })

    