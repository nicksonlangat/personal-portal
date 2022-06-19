from rest_framework import serializers
from .models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=['id', 'name', 'image']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields=['id','category','amount','created_at']

    def to_representation(self, instance):
        rep = super(ItemSerializer, self).to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep
