from django.shortcuts import render
from .models import Project
# Create your views here.

def portal_index(request):
    projects=Project.objects.all()
    context={
        'projects':projects,
    }
    return render(request, 'portfolio/index.html', context)
