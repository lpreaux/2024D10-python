from dataclasses import dataclass
import random
from typing import Optional

from .pokemon_type import PokemonType


@dataclass
class PokemonSet:
    primary_type: PokemonType
    secondary_type: Optional[PokemonType] = None

    def __str__(self):
        primary = str(self.primary_type)
        secondary = f" - {self.secondary_type}" if self.secondary_type else ""
        return primary + secondary


class Pokemon:
    def __init__(self, pokemon_name: str, hp: int, atk:int, defense: int,  primary_type: PokemonType, secondary_type: Optional[PokemonType] = None):
        self.__name: str = pokemon_name
        self.__types: PokemonSet = PokemonSet(primary_type, secondary_type)
        self.__max_hp: int = hp
        self.__hp: int = hp
        self.__atk: int = atk
        self.__defense: int = defense

    @property
    def name(self):
        return self.__name

    @property
    def types(self):
        return self.__types

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            raise ValueError("HP must be positive")
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @property
    def defense(self):
        return self.__defense

    def __str__(self) -> str:
        return f"{self.name}<HP: {self.hp}, Atk: {self.atk}, Type: {self.types}>"

    def calculate_damage_multiplier(self, attack_type: PokemonType) -> float:
        primary_multiplier = attack_type.calculate_damage_multiplier(self.__types.primary_type)
        if not self.__types.secondary_type:
            return primary_multiplier

        secondary_multiplier = attack_type.calculate_damage_multiplier(self.__types.secondary_type)
        return primary_multiplier * secondary_multiplier

    def attack(self, pokemon: 'Pokemon', move_power: int = 55):
        primary_damage_multiplier = pokemon.calculate_damage_multiplier(self.types.primary_type)
        secondary_damage_multiplier = (
            pokemon.calculate_damage_multiplier(self.types.secondary_type)
            if self.types.secondary_type else 1
        )

        random_factor = random.uniform(0.85, 1.0)

        # Simplified damage formula with higher base damage
        damage = ((2 * move_power * (self.atk / pokemon.defense)) / 5 + 2)  # Changed from 50 to 5
        damage *= primary_damage_multiplier * secondary_damage_multiplier * random_factor
        pokemon.hp = max(0, round(pokemon.hp - damage))
