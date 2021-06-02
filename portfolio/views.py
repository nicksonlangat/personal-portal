from django.shortcuts import render

# Create your views here.

def portal_index(request):
    context={
        
    }
    return render(request, 'portfolio/index.html', context)
