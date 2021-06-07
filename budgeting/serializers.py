from rest_framework import serializers
from .models import ExpenseName,Expense,Saving

class ExpenseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseName
        fields=('id','name')

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=('id','user','expense','amount_allocated')

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Saving
        fields=('id','user','month','amount_to_save')