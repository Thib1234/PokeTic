from django.urls import path
from .views import PokemonViewSet, TypeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pokemons', PokemonViewSet, basename='pokemon')
router.register(r'types', TypeViewSet, basename='type')

urlpatterns = router.urls
