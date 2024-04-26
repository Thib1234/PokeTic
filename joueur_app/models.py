from django.db import models
from pokemon_app.models import Pokemon, Type  # Importez le modèle Pokemon de pokemon_app
from arena_app.models import Badge


class Joueur(models.Model):
    nom = models.CharField(max_length=50)
    argent = models.IntegerField()
    pokemons = models.ManyToManyField(Pokemon, blank=True)  # Utilisez le modèle Pokemon importé
    badges = models.ManyToManyField(Badge, blank=True)
