from django.db import models
import calendar
from accounts.models import User
# Create your models here.

MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]

class ExpenseName(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    expense=models.ForeignKey('ExpenseName', on_delete=models.CASCADE)
    amount_allocated=models.FloatField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.expense.name

class Saving(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    month=models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    amount_to_save=models.FloatField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.month