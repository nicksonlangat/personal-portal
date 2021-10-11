from django.db import models

# Create your models here.

class Bank(models.Model):
    name=models.CharField(max_length=250, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Branch(models.Model):
    bank=models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch_code=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
