import os

from .battle import Battle
from .core import PokemonFactory
from .game import Game
from .session.session import Session

# def simulate_battle(pokemon1, pokemon2):
#     battle = Battle(pokemon1, pokemon2)
#     battle.start_battle()
#
#
#
# if __name__ == '__main__':
#     # Charger les données des Pokémon
#     file_path = os.path.join(os.path.dirname(__file__), "../data/pokemon_data.json")
#     data = PokemonFactory.load_pokemon_data(file_path)
#
#     # Créer des Pokémon
#     pikachu = PokemonFactory.create_pokemon("Pikachu", data)
#     bulbasaur = PokemonFactory.create_pokemon("Bulbasaur", data)
#     squirtle = PokemonFactory.create_pokemon("Squirtle", data)
#     charmander = PokemonFactory.create_pokemon("Charmander", data)
#     charizard = PokemonFactory.create_pokemon("Charizard", data)
#     venusaur = PokemonFactory.create_pokemon("Venusaur", data)
#     raticate = PokemonFactory.create_pokemon("Raticate", data)
#     fearow = PokemonFactory.create_pokemon("Fearow", data)
#
#     # Liste des combats prolongés
#     battles = [
#         (pikachu, bulbasaur),
#         (squirtle, charmander),
#         (charizard, venusaur),
#         (raticate, fearow),
#     ]
#
#     print("\n🔥 Bienvenue dans l'Arène Pokémon ! 🔥")
#     for pokemon1, pokemon2 in battles:
#         # Réinitialiser les HP pour chaque combat (facultatif si les HP sont partagés)
#         pokemon1.hp = data[pokemon1.name]["hp"]
#         pokemon2.hp = data[pokemon2.name]["hp"]
#
#         simulate_battle(pokemon1, pokemon2)

if __name__ == '__main__':
    game = Game()
    game.start_game()
