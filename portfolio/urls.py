from django.urls import path
from .import views

urlpatterns = [
    path('', views.portal_index),
    path('resume', views.download, name='resume'),
]
