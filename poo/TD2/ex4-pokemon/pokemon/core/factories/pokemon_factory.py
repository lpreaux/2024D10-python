import json
from typing import Dict

from ..pokemon import Pokemon
from ..pokemon_type import PokemonTypes
from .pokemon_type_factory import PokemonTypeFactory


class PokemonFactory:
    @staticmethod
    def load_pokemon_data(filepath: str) -> Dict:
        with open(filepath, 'r') as file:
            return json.load(file)

    @staticmethod
    def create_pokemon(name: str, data: Dict) -> Pokemon:
        pokemon_info = data.get(name)
        if not pokemon_info:
            raise ValueError(f"Unkwon Pokemon: {name}")

        types = [PokemonTypeFactory.get_type(getattr(PokemonTypes, t)) for t in pokemon_info["types"]]
        return Pokemon(
            pokemon_name=name,
            hp=pokemon_info["hp"],
            atk=pokemon_info["atk"],
            defense=pokemon_info["defense"],
            primary_type=types[0],
            secondary_type=types[1] if len(types) > 1 else None
        )
