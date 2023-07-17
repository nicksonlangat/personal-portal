from django.db import models

# Create your models here.
class Project(models.Model):
    TYPE_CHOICES = [
        ("template", "template"),
        ("project", "project")
    ]
    name=models.CharField(max_length=20)
    description=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='PROJECTS')
    live_link=models.CharField(max_length=100, null=True, blank=True)
    type=models.CharField(choices=TYPE_CHOICES, max_length=100, null=True, blank=True)
    code_link=models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    is_clone = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Notification(models.Model):
    title=models.CharField(max_length=250)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name

