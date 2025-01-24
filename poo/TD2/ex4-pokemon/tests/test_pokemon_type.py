# Test généré avec Claude par curiosité

import unittest
from ..pokemon.pokemon_type import PokemonType, PokemonTypes

class TestPokemonType(unittest.TestCase):
    def setUp(self):
        # Initialiser tous les types
        self.types = {t: PokemonType(t) for t in PokemonTypes}

    def test_initialization(self):
        for type_enum in PokemonTypes:
            pokemon_type = self.types[type_enum]
            self.assertEqual(pokemon_type.type, type_enum)
            self.assertIsInstance(pokemon_type.super_effective_against, set)
            self.assertIsInstance(pokemon_type.not_effective_against, set)
            self.assertIsInstance(pokemon_type.immune_against, set)

    def test_normal_effectiveness(self):
        test_cases = [
            (PokemonTypes.FIRE, PokemonTypes.NORMAL),
            (PokemonTypes.WATER, PokemonTypes.DRAGON),
            (PokemonTypes.ELECTRIC, PokemonTypes.FIRE)
        ]
        for attacker, defender in test_cases:
            self.assertEqual(
                self.types[attacker].calculate_damage_multiplier(self.types[defender]),
                PokemonType.NORMAL_DAMAGE_MULTIPLIER
            )

    def test_super_effectiveness(self):
        test_cases = [
            (PokemonTypes.FIRE, PokemonTypes.GRASS),
            (PokemonTypes.WATER, PokemonTypes.FIRE),
            (PokemonTypes.ELECTRIC, PokemonTypes.WATER),
            (PokemonTypes.GRASS, PokemonTypes.WATER),
            (PokemonTypes.ICE, PokemonTypes.DRAGON),
            (PokemonTypes.FIGHTING, PokemonTypes.NORMAL),
            (PokemonTypes.POISON, PokemonTypes.BUG),
            (PokemonTypes.GROUND, PokemonTypes.ROCK),
            (PokemonTypes.FLYING, PokemonTypes.FIGHTING),
            (PokemonTypes.PSYCHIC, PokemonTypes.POISON),
            (PokemonTypes.BUG, PokemonTypes.PSYCHIC),
            (PokemonTypes.ROCK, PokemonTypes.FLYING),
            (PokemonTypes.GHOST, PokemonTypes.GHOST),
            (PokemonTypes.DRAGON, PokemonTypes.DRAGON)
        ]
        for attacker, defender in test_cases:
            self.assertEqual(
                self.types[attacker].calculate_damage_multiplier(self.types[defender]),
                PokemonType.SUPER_EFFECTIVE_MULTIPLIER
            )

    def test_not_effective(self):
        test_cases = [
            (PokemonTypes.NORMAL, PokemonTypes.ROCK),
            (PokemonTypes.FIRE, PokemonTypes.WATER),
            (PokemonTypes.WATER, PokemonTypes.GRASS),
            (PokemonTypes.ELECTRIC, PokemonTypes.GRASS),
            (PokemonTypes.GRASS, PokemonTypes.FIRE),
            (PokemonTypes.ICE, PokemonTypes.WATER),
            (PokemonTypes.FIGHTING, PokemonTypes.PSYCHIC),
            (PokemonTypes.POISON, PokemonTypes.GHOST),
            (PokemonTypes.GROUND, PokemonTypes.GRASS),
            (PokemonTypes.FLYING, PokemonTypes.ROCK),
            (PokemonTypes.PSYCHIC, PokemonTypes.PSYCHIC),
            (PokemonTypes.BUG, PokemonTypes.GHOST),
            (PokemonTypes.ROCK, PokemonTypes.FIGHTING)
        ]
        for attacker, defender in test_cases:
            self.assertEqual(
                self.types[attacker].calculate_damage_multiplier(self.types[defender]),
                PokemonType.NOT_EFFECTIVE_MULTIPLIER
            )

    def test_immunities(self):
        test_cases = [
            (PokemonTypes.NORMAL, PokemonTypes.GHOST),
            (PokemonTypes.GHOST, PokemonTypes.NORMAL),
            (PokemonTypes.ELECTRIC, PokemonTypes.GROUND),
            (PokemonTypes.GROUND, PokemonTypes.FLYING),
            (PokemonTypes.FIGHTING, PokemonTypes.GHOST),
            (PokemonTypes.PSYCHIC, PokemonTypes.GHOST)
        ]
        for attacker, defender in test_cases:
            self.assertEqual(
                self.types[attacker].calculate_damage_multiplier(self.types[defender]),
                PokemonType.IMMUNE_MULTIPLIER
            )

    def test_relations_consistency(self):
        for type_enum in PokemonTypes:
            pokemon_type = self.types[type_enum]
            relations = PokemonType.TYPE_RELATIONS[type_enum]

            # Vérifier que tous les sets dans les relations sont corrects
            self.assertEqual(pokemon_type.super_effective_against, relations["super_effective"])
            self.assertEqual(pokemon_type.not_effective_against, relations["not_effective"])
            self.assertEqual(pokemon_type.immune_against, relations["immune"])

            # Vérifier qu'un type n'apparaît pas dans plusieurs catégories
            all_affected_types = (
                    relations["super_effective"] |
                    relations["not_effective"] |
                    relations["immune"]
            )
            self.assertEqual(
                len(all_affected_types),
                len(relations["super_effective"]) +
                len(relations["not_effective"]) +
                len(relations["immune"])
            )


if __name__ == '__main__':
    unittest.main()