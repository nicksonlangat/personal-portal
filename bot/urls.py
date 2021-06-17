from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'images', views.ImageViewset)

urlpatterns = [
    path('', views.start_up),
    path('start', views.start),
    path('place_order', views.place_order),
    path('complete_order', views.complete_order),
    path('completed_order', views.completed_order),
    path('make_payment', views.make_payment),
    path('collect_order', views.collect_order),
    path('get_shop', views.get_shop_poster),
    path('api/', include(router.urls)),
    path('push', views.push),
    path('shops', views.shops),
    path('pay', views.pay),
    path('commands', views.commands),
    path('continue_collect_order', views.continue_collect_order),
    path('almost_complete_order', views.almost_complete_order)
]

