from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'articles', views.PostViewset)
router.register(r'categories', views.CategoryViewset)
router.register(r'tags', views.TagViewset)


urlpatterns = [
    path('', include(router.urls)),]