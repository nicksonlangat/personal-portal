from django.db import models

# Create your models here.

class County(models.Model):
    name=models.CharField(max_length=250, unique=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

class Constituency(models.Model):
    county=models.ForeignKey(County, on_delete=models.CASCADE)
    name=models.CharField(max_length=250, unique=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

class Ward(models.Model):
    constituency=models.ForeignKey(Constituency, on_delete=models.CASCADE)
    name=models.CharField(max_length=250, unique=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)
