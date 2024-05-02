from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from joueur_app.models import Joueur


class Command(BaseCommand):
    help = 'Crée un joueur'

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(username='thib')
        Joueur.objects.get_or_create(user=user, defaults={'argent': 0})
        self.stdout.write(self.style.SUCCESS('Joueur créé avec succès'))
