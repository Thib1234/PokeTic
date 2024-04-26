from django.db import models


class Badge(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Arene(models.Model):
    nom = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    badge = models.OneToOneField(Badge, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom
