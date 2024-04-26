from django.db import models
from pokemon_app.models import Pokemon


class Combat(models.Model):
    pokemons = models.ManyToManyField(Pokemon)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Combat du {self.date}"
