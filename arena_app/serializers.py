from rest_framework import serializers
from .models import Badge, Arene


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge
        fields = ['url', 'nom']


class AreneSerializer(serializers.HyperlinkedModelSerializer):
    badge = BadgeSerializer()

    class Meta:
        model = Arene
        fields = ['url', 'nom', 'region', 'badge']
