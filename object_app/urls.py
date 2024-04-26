from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TypeObjetViewSet, ObjetViewSet

router = DefaultRouter()
router.register(r'typeobjets', TypeObjetViewSet)
router.register(r'objets', ObjetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
