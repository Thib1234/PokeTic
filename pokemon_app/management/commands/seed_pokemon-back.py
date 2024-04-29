from django.core.management.base import BaseCommand
from django.core.cache import cache
import requests
from pokemon_app.models import Pokemon, Type


class Command(BaseCommand):
    help = 'Populate database with Pokemon data'

    def fetch_data_from_api(self, url):
        """ Fetch and cache data from the API to minimize repeated requests. """
        data = cache.get(url)
        if not data:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                cache.set(url, data, timeout=86400)  # Cache for one day
            else:
                response.raise_for_status()
        return data

    def get_or_create_pokemon(self, data, french_name):
        """ Create or retrieve a Pokémon with its basic data, handling cases where data might be incomplete. """
        try:
            hp = data['stats'][0]['base_stat']
            experience = data['base_experience']
            attack = data['stats'][1]['base_stat']
            defense = data['stats'][2]['base_stat']
            speed = data['stats'][5]['base_stat']
            image = data['sprites']['front_default']
        except KeyError as e:
            self.stderr.write(f"Key error in data for Pokémon {french_name}: {e}")
            return None, False

        pokemon, created = Pokemon.objects.get_or_create(
            Nom=french_name,
            defaults={
                'Hp': hp,
                'Experience': experience,
                'Attaque': attack,
                'Defense': defense,
                'Vitesse': speed,
                'Image': image,
            }
        )
        return pokemon, created

    def handle(self, *args, **options):
        for i in range(1, 152):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            species_url = f'https://pokeapi.co/api/v2/pokemon-species/{i}'

            try:
                data = self.fetch_data_from_api(pokemon_url)
                species_data = self.fetch_data_from_api(species_url)

                french_name = next(
                    (name['name'] for name in species_data['names'] if name['language']['name'] == 'fr'),
                    data['name']
                )

                pokemon, created = self.get_or_create_pokemon(data, french_name)
                if not created:
                    continue

                for type_data in data['types']:
                    type_name = type_data['type']['name']
                    type_obj, _ = Type.objects.get_or_create(Nom=type_name)
                    pokemon.types.add(type_obj)

                if species_data.get('evolves_from_species'):
                    pre_species_data = self.fetch_data_from_api(species_data['evolves_from_species']['url'])
                    pre_french_name = next(
                        (name['name'] for name in pre_species_data['names'] if name['language']['name'] == 'fr'),
                        pre_species_data['name']
                    )
                    pre_pokemon, _ = self.get_or_create_pokemon(pre_species_data, pre_french_name)
                    if pre_pokemon is not None:
                        pokemon.evolves_from_id = pre_pokemon.id
                        pokemon.save()

                if species_data.get('evolution_chain'):
                    chain_data = self.fetch_data_from_api(species_data['evolution_chain']['url'])
                    self.handle_evolution_chain(chain_data, data['name'], pokemon)

            except requests.RequestException as e:
                self.stderr.write(f"API request failed for Pokémon ID {i}: {e}")

    def handle_evolution_chain(self, chain_data, current_name, pokemon):
        current_evolution = chain_data['chain']
        while current_evolution and current_evolution['species']['name'] != current_name:
            current_evolution = current_evolution['evolves_to'][0] if current_evolution['evolves_to'] else None

        if current_evolution and current_evolution['evolves_to']:
            for evolution in current_evolution['evolves_to']:
                species_data = self.fetch_data_from_api(evolution['species']['url'])
                french_name = next(
                    (name['name'] for name in species_data['names'] if name['language']['name'] == 'fr'),
                    species_data['name']
                )
                evolved_pokemon, _ = self.get_or_create_pokemon(species_data, french_name)
                if evolved_pokemon is not None:
                    pokemon.evolves_to_id = evolved_pokemon.id
                    pokemon.save()
