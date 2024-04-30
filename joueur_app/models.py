from django.db import models
from pokemon_app.models import Pokemon
from arena_app.models import Badge


class Joueur(models.Model):
    username = models.CharField(max_length=50)
    argent = models.IntegerField()
    pokemons = models.ManyToManyField(Pokemon, blank=True)
    badges = models.ManyToManyField(Badge, blank=True)
    password = models.CharField(max_length=128)
