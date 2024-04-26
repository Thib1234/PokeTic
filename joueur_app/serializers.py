from rest_framework import serializers
from .models import Joueur
from pokemon_app.serializers import PokemonSerializer
from arena_app.serializers import BadgeSerializer


class JoueurSerializer(serializers.ModelSerializer):
    pokemons = PokemonSerializer(many=True)
    badges = BadgeSerializer(many=True)

    class Meta:
        model = Joueur
        fields = ['nom', 'argent', 'pokemons', 'badges']
