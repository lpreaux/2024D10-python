import unittest
from ..pokemon import Pikachu, Charizard
from ..pokemon.pokemon_type import PokemonType, PokemonTypes

class TestPokemon(unittest.TestCase):
    # Tests using Pikachu (mono-type) and Charizard (dual-type) as examples
    def setUp(self):
        self.pikachu = Pikachu()
        self.charizard = Charizard()

    def test_init_mono_type(self):
        self.assertEqual(self.pikachu.name, 'Pikachu')
        self.assertEqual(self.pikachu.types.primary_type.type, PokemonTypes.ELECTRIC)
        self.assertIsNone(self.pikachu.types.secondary_type)

    def test_init_double_type(self):
        self.assertEqual(self.charizard.name, 'Charizard')
        self.assertEqual(self.charizard.types.primary_type.type, PokemonTypes.FIRE)
        self.assertEqual(self.charizard.types.secondary_type.type, PokemonTypes.FLYING)

    def test_damage_multipliers_mono_type(self):
        ground_type = PokemonType(PokemonTypes.GROUND)
        electric_type = PokemonType(PokemonTypes.ELECTRIC)
        grass_type = PokemonType(PokemonTypes.GRASS)

        # Ground is super effective vs Electric
        self.assertEqual(self.pikachu.calculate_damage_multiplier(ground_type), 2.0)
        # Electric is not very effective vs Electric
        self.assertEqual(self.pikachu.calculate_damage_multiplier(electric_type), 0.5)
        # Grass is neutral vs Electric
        self.assertEqual(self.pikachu.calculate_damage_multiplier(grass_type), 1.0)

    def test_damage_multipliers_double_type(self):
        water_type = PokemonType(PokemonTypes.WATER)
        rock_type = PokemonType(PokemonTypes.ROCK)
        grass_type = PokemonType(PokemonTypes.GRASS)

        # Water is super effective vs Fire, neutral vs Flying = 2.0
        self.assertEqual(self.charizard.calculate_damage_multiplier(water_type), 2.0)
        # Rock is super effective vs both Fire and Flying = 4.0
        self.assertEqual(self.charizard.calculate_damage_multiplier(rock_type), 4.0)
        # Grass is not effective vs both Fire and Flying = 0.25
        self.assertEqual(self.charizard.calculate_damage_multiplier(grass_type), 0.25)

if __name__ == '__main__':
    unittest.main()