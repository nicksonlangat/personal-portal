from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', views.CategoryViewset)
router.register(r'items', views.ItemViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('data',views.CombinedData.as_view(),name='data'),
    ]