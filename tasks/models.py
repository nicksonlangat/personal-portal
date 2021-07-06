from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    # is_complete=models.BooleanField(default=False)

    def __str__(self):
        return self.title
