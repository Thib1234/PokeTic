from rest_framework import serializers
from .models import TypeObjet, Objet


class TypeObjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeObjet
        fields = ['nom']


class ObjetSerializer(serializers.ModelSerializer):
    type_objet = TypeObjetSerializer()

    class Meta:
        model = Objet
        fields = ['nom', 'description', 'effet', 'type_objet']
