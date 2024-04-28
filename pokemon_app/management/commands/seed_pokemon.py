from django.core.management.base import BaseCommand
import requests
from pokemon_app.models import Pokemon, Type


class Command(BaseCommand):
    help = 'Populate database with Pokemon data'

    def handle(self, *args, **options):
        for i in range(1, 152):
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
            data = response.json()

            species_response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{i}')
            species_data = species_response.json()
            french_name = next((name['name'] for name in species_data['names'] if name['language']['name'] == 'fr'),
                               data['name'])

            pokemon = Pokemon(
                Nom=french_name,
                Hp=data['stats'][0]['base_stat'],
                Experience=data['base_experience'],
                Attaque=data['stats'][1]['base_stat'],
                Defense=data['stats'][2]['base_stat'],
                Vitesse=data['stats'][5]['base_stat'],
                Image=data['sprites']['front_default'],
            )

            pokemon.save()

            for type_data in data['types']:
                type_name = type_data['type']['name']
                type_obj, created = Type.objects.get_or_create(Nom=type_name)

                pokemon.types.add(type_obj)


            if species_data['evolves_from_species']:
                species_response = requests.get(species_data['evolves_from_species']['url'])
                pre_species_data = species_response.json()

                if pre_species_data and 'names' in pre_species_data:
                    pre_evolution_french_name = next(
                        (name['name'] for name in pre_species_data['names'] if name['language']['name'] == 'fr'),
                        pre_species_data['name'])
                    pre_evolution, _ = Pokemon.objects.get_or_create(Nom=pre_evolution_french_name)

                    pokemon.evolves_from = pre_evolution
                    pokemon.save()

