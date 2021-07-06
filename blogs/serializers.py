from rest_framework import serializers
from .models import Category, Post,Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['id','title']

class PostSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Post
        fields=['id','title','category','content','image','created','tags','author']
