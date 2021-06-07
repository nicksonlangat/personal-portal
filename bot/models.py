from django.db import models

# Create your models here.
class Merchant(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=20)
    merchant=models.ForeignKey('Merchant', on_delete=models.CASCADE)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product=models.ForeignKey('Product', on_delete=models.CASCADE)
    customer=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product


class Image(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.name