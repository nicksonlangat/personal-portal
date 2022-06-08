from django.shortcuts import render
from .models import Project
import requests
import os
from django.conf import settings
from django.http import HttpResponse, Http404

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
    projects=Project.objects.all()
    posts = requests.get('https://dev.to/api/articles?username=nick_langat').json()
    context={
        'projects':projects,
        'posts':posts
    }
    return render(request, 'portfolio/index.html', context)
