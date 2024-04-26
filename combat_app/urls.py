from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CombatViewSet

router = DefaultRouter()
router.register(r'combats', CombatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
