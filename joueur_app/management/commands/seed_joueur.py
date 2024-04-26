from django.core.management.base import BaseCommand
from joueur_app.models import Joueur


class Command(BaseCommand):
    help = 'Crée un joueur'

    def handle(self, *args, **kwargs):
        Joueur.objects.get_or_create(nom='thib', defaults={'argent': 0})
        self.stdout.write(self.style.SUCCESS('Joueur créé avec succès'))
