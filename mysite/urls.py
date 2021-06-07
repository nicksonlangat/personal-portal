from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('budgeting/api/v1/', include('budgeting.urls')),
    path('bot/', include('bot.urls')),
]
