from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to='PROJECTS')
    live_link=models.CharField(max_length=100)
    code_link=models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    is_clone = models.BooleanField(default=False)

    def __str__(self):
        return self.name