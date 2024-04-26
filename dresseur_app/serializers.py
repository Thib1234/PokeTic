from rest_framework import serializers
from .models import PNJ, Ligue

class PNJSerializer(serializers.ModelSerializer):
    class Meta:
        model = PNJ
        fields = ['nom', 'argent', 'phrase_accroche', 'est_champion', 'arene']

class LigueSerializer(serializers.ModelSerializer):
    champion = PNJSerializer()

    class Meta:
        model = Ligue
        fields = ['nom', 'champion']
