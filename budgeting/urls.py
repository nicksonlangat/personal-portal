from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

router.register(r'expensenames', views.ExpenseNameViewset)
router.register(r'expenses', views.ExpenseViewset)
router.register(r'savings', views.SavingViewset)

urlpatterns = [
    path('', include(router.urls)),
]