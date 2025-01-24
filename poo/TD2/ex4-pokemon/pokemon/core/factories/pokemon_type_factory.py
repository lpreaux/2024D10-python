from typing import Dict

from ..pokemon_type import PokemonType, PokemonTypes


class PokemonTypeFactory:
    _instance: Dict = {}

    @classmethod
    def get_type(cls, pokemon_type: PokemonTypes):
        if pokemon_type not in cls._instance:
            cls._instance[pokemon_type] = PokemonType(pokemon_type)
        return cls._instance[pokemon_type]