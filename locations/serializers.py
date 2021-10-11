from rest_framework import serializers
from .models import County, Constituency, Ward

class CountySerializer(serializers.ModelSerializer):
    constituencies=serializers.SerializerMethodField(read_only=True)
    wards=serializers.SerializerMethodField(read_only=True)

    def get_constituencies(self,obj):
        total=Constituency.objects.filter(county=obj).count()
        return total
    def get_wards(self,obj):
        total=Ward.objects.filter(constituency__county=obj).count()
        return total
    class Meta:
        model=County
        fields=['id', 'name', 'constituencies', 'wards']

class ConstituencySerializer(serializers.ModelSerializer):
    wards=serializers.SerializerMethodField(read_only=True)
    def get_wards(self,obj):
        total=Ward.objects.filter(constituency=obj).count()
        return total
    class Meta:
        model=Constituency
        fields=['id','county', 'name', 'wards']
    
    def to_representation(self, instance):
        rep = super(ConstituencySerializer, self).to_representation(instance)
        rep['county'] = instance.county.name
        return rep

class WardSerializer(serializers.ModelSerializer):
    county=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Ward
        fields=['id','constituency','name', 'county']

    
    def to_representation(self, instance):
        rep = super(WardSerializer, self).to_representation(instance)
        rep['constituency'] = instance.constituency.name
        return rep

    def get_county(self,obj):
        cx=obj.constituency
        return cx.county.name
        
