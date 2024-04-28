from django.db import models


class Type(models.Model):
    Nom = models.CharField(max_length=50)
    points_forts = models.ManyToManyField('self', related_name='points_faibles', symmetrical=False)

    def __str__(self):
        return self.Nom


class Talent(models.Model):
    Nom = models.CharField(max_length=50)
    tc = models.BooleanField()

    def __str__(self):
        return self.Nom


class Pokemon(models.Model):
    Nom = models.CharField(max_length=50, unique=True)
    Hp = models.IntegerField(null=True)
    Experience = models.IntegerField(null=True)
    Attaque = models.IntegerField(null=True)
    Defense = models.IntegerField(null=True)
    Vitesse = models.IntegerField(null=True)
    Image = models.CharField(max_length=500)
    types = models.ManyToManyField(Type)
    talents = models.ManyToManyField(Talent)
    evolves_from = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='evolves_to')

    def __str__(self):
        return self.Nom
