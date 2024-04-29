from django.core.management.base import BaseCommand
from django.core.cache import cache
import requests
from pokemon_app.models import Pokemon, Type, Talent

POKEAPI_URL = "https://pokeapi.co/api/v2/"


def get_pokemon_data(pokemon_name):
    response = requests.get(f"{POKEAPI_URL}pokemon/{pokemon_name}")
    return response.json()


def get_type_data(type_name):
    response = requests.get(f"{POKEAPI_URL}type/{type_name}")
    return response.json()


def get_evolution_chain(chain_id):
    response = requests.get(f"{POKEAPI_URL}evolution-chain/{chain_id}")
    return response.json()


def handle_evolution_chain(chain, evolves_from=None):
    # Récupérer les données du Pokémon
    pokemon_data = get_pokemon_data(chain['species']['name'])

    # Ignorer les Pokémon dont l'ID est supérieur à 151
    if pokemon_data['id'] > 151:
        return

    # Créer un nouvel objet Pokemon pour l'espèce actuelle
    pokemon, created = Pokemon.objects.get_or_create(
        Nom=pokemon_data['name'],
        Hp=pokemon_data['stats'][0]['base_stat'],
        Experience=pokemon_data['base_experience'],
        Attaque=pokemon_data['stats'][1]['base_stat'],
        Defense=pokemon_data['stats'][2]['base_stat'],
        Vitesse=pokemon_data['stats'][5]['base_stat'],
        Image=pokemon_data['sprites']['front_default'],
        evolves_from=evolves_from,
    )

    # Ajouter les types et les talents
    for type_data in pokemon_data['types']:
        type, created = Type.objects.get_or_create(Nom=type_data['type']['name'])
        pokemon.types.add(type)

    for ability_data in pokemon_data['abilities']:
        talent, created = Talent.objects.get_or_create(Nom=ability_data['ability']['name'])
        pokemon.talents.add(talent)

    pokemon.save()

    # Parcourir toutes les évolutions possibles
    for evolution in chain['evolves_to']:
        next_pokemon = handle_evolution_chain(evolution, evolves_from=pokemon)
        pokemon.evolves_to = next_pokemon
        pokemon.save()

    return pokemon


class Command(BaseCommand):
    help = 'Populates the database with Pokemon data from the PokeAPI'

    def handle(self, *args, **options):
        self.stdout.write('Starting to populate the database...')
        for i in range(1, 152):
            self.stdout.write(f"Processing evolution chain {i}...")
            chain_data = get_evolution_chain(i)
            handle_evolution_chain(chain_data['chain'])

        for type_name in ['grass', 'poison', 'fire', 'flying', 'water', 'bug', 'normal', 'ground', 'fighting',
                          'psychic', 'rock', 'electric', 'steel', 'ice', 'ghost', 'dragon']:
            self.stdout.write(f"Processing type {type_name}...")
            type_data = get_type_data(type_name)

            type, created = Type.objects.get_or_create(Nom=type_data['name'])

            for damage_relation in type_data['damage_relations']['double_damage_to']:
                point_fort, created = Type.objects.get_or_create(Nom=damage_relation['name'])
                type.points_forts.add(point_fort)
            for damage_relation in type_data['damage_relations']['double_damage_from']:
                point_faible, created = Type.objects.get_or_create(Nom=damage_relation['name'])
                type.points_faibles.add(point_faible)

            type.save()

        self.stdout.write('Finished populating the database.')
