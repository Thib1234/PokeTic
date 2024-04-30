from rest_framework import serializers
from .models import Joueur
from arena_app.models import Badge


class JoueurSerializer(serializers.ModelSerializer):
    pokemons = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pokemon-detail'
    )
    badges = serializers.PrimaryKeyRelatedField(many=True, queryset=Badge.objects.all(), required=False)

    class Meta:
        model = Joueur
        fields = ['nom', 'argent', 'pokemons', 'badges']
