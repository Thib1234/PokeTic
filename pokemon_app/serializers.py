from rest_framework import serializers
from .models import Pokemon, Type


class PokemonSerializer(serializers.ModelSerializer):
    types = serializers.StringRelatedField(many=True)

    class Meta:
        model = Pokemon
        fields = ['Nom', 'Hp', 'Experience', 'Attaque', 'Defense', 'Vitesse', 'types']


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['Nom']
