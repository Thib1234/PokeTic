from django.db import models
from pokemon_app.models import Pokemon, Type
from arena_app.models import Badge


class Joueur(models.Model):
    nom = models.CharField(max_length=50)
    argent = models.IntegerField()
    pokemons = models.ManyToManyField(Pokemon, blank=True)
    badges = models.ManyToManyField(Badge, blank=True)
