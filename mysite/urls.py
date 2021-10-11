from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('budgeting/api/v1/', include('budgeting.urls')),
    path('bot/', include('bot.urls')),
    path('tasks/', include('tasks.urls')),
    path('blogs/', include('blogs.urls')),
     path('events/', include('events.urls')),
     path('locations/', include('locations.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
