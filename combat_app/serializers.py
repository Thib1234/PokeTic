from rest_framework import serializers
from .models import Combat
from pokemon_app.serializers import PokemonSerializer


class CombatSerializer(serializers.ModelSerializer):
    pokemons = PokemonSerializer(many=True)

    class Meta:
        model = Combat
        fields = ['pokemons', 'date']
