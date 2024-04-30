from rest_framework import serializers
from pokemon_app.models import Pokemon
from .models import Joueur
from arena_app.models import Badge


class JoueurSerializer(serializers.ModelSerializer):
    pokemons = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Pokemon.objects.all(),
        required=False
    )
    badges = serializers.PrimaryKeyRelatedField(many=True, queryset=Badge.objects.all(), required=False)

    class Meta:
        model = Joueur
        fields = ['username', 'argent', 'pokemons', 'badges', 'password']
