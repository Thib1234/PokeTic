from django.db import models


class Type(models.Model):
    Nom = models.CharField(max_length=50)

    def __str__(self):
        return self.Nom


class Pokemon(models.Model):
    Nom = models.CharField(max_length=50)
    Hp = models.IntegerField()
    Experience = models.IntegerField()
    Attaque = models.IntegerField()
    Defense = models.IntegerField()
    Vitesse = models.IntegerField()
    types = models.ManyToManyField(Type)

    def __str__(self):
        return self.Nom
