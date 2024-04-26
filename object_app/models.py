from django.db import models


class TypeObjet(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Objet(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    effet = models.TextField()
    type_objet = models.ForeignKey(TypeObjet, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
