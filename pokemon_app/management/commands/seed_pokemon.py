from django.core.management.base import BaseCommand
import requests
from pokemon_app.models import Pokemon, Type


class Command(BaseCommand):
    help = 'Populate database with Pokemon data'

    def handle(self, *args, **options):
        for i in range(1, 152):
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
            data = response.json()

            pokemon = Pokemon(
                Nom=data['name'],
                Hp=data['stats'][0]['base_stat'],
                Experience=data['base_experience'],
                Attaque=data['stats'][1]['base_stat'],
                Defense=data['stats'][2]['base_stat'],
                Vitesse=data['stats'][5]['base_stat'],
            )

            pokemon.save()

            for type_data in data['types']:
                type_name = type_data['type']['name']
                type_obj, created = Type.objects.get_or_create(Nom=type_name)

                pokemon.types.add(type_obj)
