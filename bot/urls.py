from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'images', views.ImageViewset)

urlpatterns = [
    path('', views.start_up),
    path('place_order', views.order),
    path('complete_order', views.complete_order),
    path('make_payment', views.make_payment),
    path('done_deal', views.done_deal),
    path('get_shop', views.get_shop_poster),
    path('api/', include(router.urls)),
    path('push', views.push),
    path('shops', views.shops),
]

