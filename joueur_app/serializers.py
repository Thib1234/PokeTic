from rest_framework import serializers
from .models import Joueur
from pokemon_app.models import Pokemon  # Importer Pokemon de pokemon_app
from arena_app.models import Badge  # Importer Badge de arena_app
from pokemon_app.serializers import PokemonSerializer
from arena_app.serializers import BadgeSerializer


class JoueurSerializer(serializers.ModelSerializer):
    pokemons = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pokemon-detail'  # Le nom de la vue de détail de Pokemon
    )
    badges = serializers.PrimaryKeyRelatedField(many=True, queryset=Badge.objects.all(), required=False)  # Rendre le champ 'badges' facultatif

    class Meta:
        model = Joueur
        fields = ['nom', 'argent', 'pokemons', 'badges']