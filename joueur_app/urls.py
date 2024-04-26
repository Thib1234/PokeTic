from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import JoueurViewSet

router = DefaultRouter()
router.register(r'joueurs', JoueurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
