from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=250
    )
    image = models.ImageField(upload_to='media/finance')

    def __str__(self) -> str:
        return str(self.name)

class Item(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return str(self.category)