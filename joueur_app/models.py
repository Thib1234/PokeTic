from django.contrib.auth.models import User
from django.db import models
from pokemon_app.models import Pokemon
from arena_app.models import Badge


class Joueur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    argent = models.IntegerField()
    pokemons = models.ManyToManyField(Pokemon, blank=True)
    badges = models.ManyToManyField(Badge, blank=True)
    password = models.CharField(max_length=128)
