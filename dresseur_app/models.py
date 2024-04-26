from django.db import models
from arena_app.models import Arene


class PNJ(models.Model):
    nom = models.CharField(max_length=50)
    argent = models.IntegerField()
    phrase_accroche = models.CharField(max_length=255)
    est_champion = models.BooleanField()
    arene = models.ForeignKey(Arene, on_delete=models.CASCADE, null=True, blank=True)


class Ligue(models.Model):
    nom = models.CharField(max_length=50)
    champion = models.OneToOneField(PNJ, on_delete=models.SET_NULL, null=True, blank=True)
