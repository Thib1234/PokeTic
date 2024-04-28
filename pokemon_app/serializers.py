from rest_framework import serializers
from .models import Pokemon, Type, Talent


class TalentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Talent
        fields = ['Nom']


class TypeSerializer(serializers.ModelSerializer):
    points_forts = serializers.StringRelatedField(many=True)
    points_faibles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Type
        fields = ['Nom', 'points_forts', 'points_faibles']


class PokemonSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True)
    talents = TalentSerializer(many=True)
    evolves_from = serializers.StringRelatedField()

    class Meta:
        model = Pokemon
        fields = ['Nom', 'Hp', 'Experience', 'Attaque', 'Defense', 'Vitesse', 'Image', 'types', 'talents',
                  'evolves_from']
