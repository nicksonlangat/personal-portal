from django.db import models

# Create your models here.
class Event(models.Model):
    COLOR_CHOICES=[ 
        ('blue','blue'),
        ('indigo','indigo'),
        ('cyan','cyan'),
        ('green','green'),
        ('orange','orange'),
        ('grey darken-1','grey darken-1'),
        ('deep-purple','deep-purple')
    ]
    name=models.CharField(max_length=250)
    details=models.TextField()
    start=models.DateField()
    end=models.DateField()
    color=models.CharField( max_length=50,
        default='blue',)

    def __str__(self):
        return self.name