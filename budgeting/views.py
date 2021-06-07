from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    ExpenseNameSerializer,
    ExpenseSerializer,
    SavingSerializer
)
from .models import (
    ExpenseName,
    Expense,
    Saving
)
# Create your views here.

class ExpenseNameViewset(viewsets.ModelViewSet):
    queryset=ExpenseName.objects.all()
    serializer_class=ExpenseNameSerializer


class ExpenseViewset(viewsets.ModelViewSet):
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer


class SavingViewset(viewsets.ModelViewSet):
    queryset=Saving.objects.all()
    serializer_class=SavingSerializer
