from django.core.management.base import BaseCommand
import requests
from object_app.models import Objet, TypeObjet


class Command(BaseCommand):
    help = 'Populate database with Pokemon data'

    def handle(self, *args, **options):
        # Faites une requête à l'API pour obtenir les données des objets
        response = requests.get('https://pokeapi.co/api/v2/item/')
        data = response.json()

        # Parcourez chaque objet dans les données
        for item_data in data['results']:
            # Faites une autre requête pour obtenir les détails de l'objet
            item_response = requests.get(item_data['url'])
            item_details = item_response.json()

            # Créez un nouveau TypeObjet pour chaque objet
            type_objet, created = TypeObjet.objects.get_or_create(nom=item_details['category']['name'])

            # Créez une nouvelle instance de Objet pour chaque objet
            Objet.objects.create(
                nom=item_details['name'],
                description=item_details['effect_entries'][0]['short_effect'],
                effet=item_details['effect_entries'][0]['effect'],
                type_objet=type_objet,
            )
