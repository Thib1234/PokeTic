from django.core.management.base import BaseCommand
from arena_app.models import Arene, Badge


class Command(BaseCommand):
    help = 'Populate database with Pokemon data'

    def handle(self, *args, **options):
        arena_names = ['Argenta', 'Azuria', 'Carmin sur Mer', 'Céladopole', 'Parmanie', 'Safrania', 'Cramois\'Île',
                       'Jadielle']

        for name in arena_names:
            badge = Badge.objects.create(nom=f"Badge de {name}")

            Arene.objects.create(nom=name, region='Kanto', badge=badge)
