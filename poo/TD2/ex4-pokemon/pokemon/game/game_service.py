import os
from typing import TYPE_CHECKING

from ..core import PokemonFactory

if TYPE_CHECKING:
    from .game import Game

class GameService:
    def __init__(self, context: 'Game'):
        self.context = context

    def should_game_init(self) -> bool:
        return True

    def initialize(self):
        file_path = os.path.join(os.path.dirname(__file__), "../../data/pokemon_data.json")
        self.context.pokemon_data = PokemonFactory.load_pokemon_data(file_path)

    def handle_player_action(self):
        action = self.context.menu.display_menu()
        command =  self.context.command_factory.create_command(action)
        return command.execute()
