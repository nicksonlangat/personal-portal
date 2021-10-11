from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'counties', views.CountyViewset)
router.register(r'constituencies', views.CostituencyViewset)
router.register(r'wards', views.WardViewset)


urlpatterns = [
    path('', include(router.urls)),]