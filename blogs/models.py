from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title=models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Post(models.Model):
    category=models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    author=models.CharField(max_length=250, null=True, blank=True)
    title=models.CharField(max_length=250)
    content=models.TextField()
    image=models.ImageField(upload_to='Blog-Images')
    created=models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-created']