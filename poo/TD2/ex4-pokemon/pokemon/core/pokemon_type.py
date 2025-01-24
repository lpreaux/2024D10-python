from enum import Enum
from typing import Set


class PokemonTypes(Enum):
    NORMAL = 'Normal'
    FIRE = 'Fire'
    WATER = 'Water'
    GRASS = 'Grass'

    # Les types suivants ont été généré par Claude
    ELECTRIC = 'Electric'
    ICE = 'Ice'
    FIGHTING = 'Fighting'
    POISON = 'Poison'
    GROUND = 'Ground'
    FLYING = 'Flying'
    PSYCHIC = 'Psychic'
    BUG = 'Bug'
    ROCK = 'Rock'
    GHOST = 'Ghost'
    DRAGON = 'Dragon'


class PokemonType:
    NORMAL_DAMAGE_MULTIPLIER = 1.0
    SUPER_EFFECTIVE_MULTIPLIER = 2.0
    NOT_EFFECTIVE_MULTIPLIER = 0.5
    IMMUNE_MULTIPLIER = 0.0

    # Première version du dictionnaire de relations entre les types fait à la main
    # TYPE_RELATIONS = {
    #     PokemonTypes.NORMAL: {
    #         "super_effective": set(),
    #         "not_effective": {PokemonTypes.ROCK},
    #         "immune": {PokemonTypes.GHOST}
    #     },
    #     PokemonTypes.FIRE: {
    #         "super_effective": {PokemonTypes.GRASS},
    #         "not_effective": {PokemonTypes.WATER},
    #         "immune": set()
    #     },
    #     PokemonTypes.WATER: {
    #         "super_effective": {PokemonTypes.FIRE},
    #         "not_effective": {PokemonTypes.GRASS},
    #         "immune": set()
    #     },
    #     PokemonTypes.GRASS: {
    #         "super_effective": {PokemonTypes.WATER},
    #         "not_effective": {PokemonTypes.FIRE},
    #         "immune": set()
    #     },
    # }

    # Version complète du tableau de relation avec tous les types de la première gen Pokemon généré avec Claude
    TYPE_RELATIONS = {
        PokemonTypes.NORMAL: {
            "super_effective": set(),
            "not_effective": {PokemonTypes.ROCK},
            "immune": {PokemonTypes.GHOST}
        },
        PokemonTypes.FIRE: {
            "super_effective": {PokemonTypes.GRASS, PokemonTypes.ICE, PokemonTypes.BUG},
            "not_effective": {PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.ROCK, PokemonTypes.DRAGON},
            "immune": set()
        },
        PokemonTypes.WATER: {
            "super_effective": {PokemonTypes.FIRE, PokemonTypes.GROUND, PokemonTypes.ROCK},
            "not_effective": {PokemonTypes.WATER, PokemonTypes.GRASS, PokemonTypes.DRAGON},
            "immune": set()
        },
        PokemonTypes.GRASS: {
            "super_effective": {PokemonTypes.WATER, PokemonTypes.GROUND, PokemonTypes.ROCK},
            "not_effective": {PokemonTypes.FIRE, PokemonTypes.GRASS, PokemonTypes.POISON, PokemonTypes.FLYING,
                              PokemonTypes.BUG, PokemonTypes.DRAGON},
            "immune": set()
        },
        PokemonTypes.ELECTRIC: {
            "super_effective": {PokemonTypes.WATER, PokemonTypes.FLYING},
            "not_effective": {PokemonTypes.GRASS, PokemonTypes.ELECTRIC, PokemonTypes.DRAGON},
            "immune": {PokemonTypes.GROUND}
        },
        PokemonTypes.ICE: {
            "super_effective": {PokemonTypes.GRASS, PokemonTypes.GROUND, PokemonTypes.FLYING, PokemonTypes.DRAGON},
            "not_effective": {PokemonTypes.WATER, PokemonTypes.ICE},
            "immune": set()
        },
        PokemonTypes.FIGHTING: {
            "super_effective": {PokemonTypes.NORMAL, PokemonTypes.ICE, PokemonTypes.ROCK},
            "not_effective": {PokemonTypes.POISON, PokemonTypes.FLYING, PokemonTypes.PSYCHIC, PokemonTypes.BUG},
            "immune": {PokemonTypes.GHOST}
        },
        PokemonTypes.POISON: {
            "super_effective": {PokemonTypes.GRASS, PokemonTypes.BUG},
            "not_effective": {PokemonTypes.POISON, PokemonTypes.GROUND, PokemonTypes.ROCK, PokemonTypes.GHOST},
            "immune": set()
        },
        PokemonTypes.GROUND: {
            "super_effective": {PokemonTypes.FIRE, PokemonTypes.ELECTRIC, PokemonTypes.POISON, PokemonTypes.ROCK},
            "not_effective": {PokemonTypes.GRASS, PokemonTypes.BUG},
            "immune": {PokemonTypes.FLYING}
        },
        PokemonTypes.FLYING: {
            "super_effective": {PokemonTypes.GRASS, PokemonTypes.FIGHTING, PokemonTypes.BUG},
            "not_effective": {PokemonTypes.ELECTRIC, PokemonTypes.ROCK},
            "immune": set()
        },
        PokemonTypes.PSYCHIC: {
            "super_effective": {PokemonTypes.FIGHTING, PokemonTypes.POISON},
            "not_effective": {PokemonTypes.PSYCHIC},
            "immune": {PokemonTypes.GHOST}
        },
        PokemonTypes.BUG: {
            "super_effective": {PokemonTypes.GRASS, PokemonTypes.PSYCHIC},
            "not_effective": {PokemonTypes.FIRE, PokemonTypes.FIGHTING, PokemonTypes.POISON, PokemonTypes.FLYING,
                              PokemonTypes.GHOST},
            "immune": set()
        },
        PokemonTypes.ROCK: {
            "super_effective": {PokemonTypes.FIRE, PokemonTypes.ICE, PokemonTypes.FLYING, PokemonTypes.BUG},
            "not_effective": {PokemonTypes.FIGHTING, PokemonTypes.GROUND},
            "immune": set()
        },
        PokemonTypes.GHOST: {
            "super_effective": {PokemonTypes.GHOST, PokemonTypes.PSYCHIC},
            "not_effective": set(),
            "immune": {PokemonTypes.NORMAL}
        },
        PokemonTypes.DRAGON: {
            "super_effective": {PokemonTypes.DRAGON},
            "not_effective": set(),
            "immune": set()
        }
    }

    def __init__(self, type_enum: PokemonTypes):
        self.type = type_enum
        relations = self.TYPE_RELATIONS[self.type]
        self.super_effective_against: Set[PokemonTypes] = relations["super_effective"]
        self.not_effective_against: Set[PokemonTypes] = relations["not_effective"]
        self.immune_against: Set[PokemonTypes] = relations["immune"]

    def calculate_damage_multiplier(self, defender_type: 'PokemonType') -> float:
        if defender_type.type in self.immune_against:
            return PokemonType.IMMUNE_MULTIPLIER
        elif defender_type.type in self.super_effective_against:
            return PokemonType.SUPER_EFFECTIVE_MULTIPLIER
        elif defender_type.type in self.not_effective_against:
            return PokemonType.NOT_EFFECTIVE_MULTIPLIER
        else:
            return PokemonType.NORMAL_DAMAGE_MULTIPLIER

    def __str__(self):
        return self.type.value
