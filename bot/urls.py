from django.urls import path
from .import views

urlpatterns = [
    path('', views.start_up),
    path('place_order', views.order),
]
