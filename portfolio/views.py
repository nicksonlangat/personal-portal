from django.shortcuts import render
from .models import Project, Notification, Message
import requests
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from rest_framework import viewsets, serializers, filters
from django_filters.rest_framework import DjangoFilterBackend


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
    
    def to_representation(self, instance):
        rep = super(NotificationSerializer, self).to_representation(instance)
        rep['message'] = MessageSerializer(instance.message).data
        return rep

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

# Create your views here.
def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'resume.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def portal_index(request):
    projects=Project.objects.filter(is_published=True)
    posts = requests.get('https://dev.to/api/articles?username=nick_langat').json()
    context={
        'projects':projects,
        'posts':posts
    }
    return render(request, 'portfolio/index.html', context)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_published=True)
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_clone',]
    search_fields = ['name']

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
   
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_read',]
    search_fields = ['title']
