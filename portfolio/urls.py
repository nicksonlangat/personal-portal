from django.urls import path
from .import views

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'api/projects', views.ProjectViewSet)
router.register(r'api/messages', views.MessageViewSet)
router.register(r'api/notifications', views.NotificationViewSet)

urlpatterns = [
    path('', views.portal_index),
    path('resume', views.download, name='resume'),
] + router.urls
