from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from blogs.models import Post, Category, Tag
from .serializers import (
    PostSerializer,
    CategorySerializer,
    TagSerializer
)
# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset=Post.objects.select_related('category').prefetch_related('tags')
    serializer_class=PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__id']
    search_fields = ['title']

class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class TagViewset(viewsets.ModelViewSet):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer