from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PNJViewSet, LigueViewSet

router = DefaultRouter()
router.register(r'pnjs', PNJViewSet)
router.register(r'ligues', LigueViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
