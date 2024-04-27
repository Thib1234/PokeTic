from rest_framework import serializers
from .models import TypeObjet, Objet


class TypeObjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeObjet
        fields = ['nom']


class ObjetSerializer(serializers.ModelSerializer):
    type_objet_url = serializers.HyperlinkedRelatedField(source='type_objet', view_name='typeobjet-detail', read_only=True)
    type_objet_nom = serializers.SlugRelatedField(source='type_objet', slug_field='nom', read_only=True)

    class Meta:
        model = Objet
        fields = ['nom', 'description', 'effet', 'type_objet_url', 'type_objet_nom']
