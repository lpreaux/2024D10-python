from abc import abstractmethod
from typing import TYPE_CHECKING

from .game_menu import MainActions
from ..session import Session

if TYPE_CHECKING:
    from .game import Game


class GameCommand:
    @abstractmethod
    def execute(self):
        pass


class StartNewSession(GameCommand):
    def __init__(self, pokemon_data: dict):
        self.pokemon_data = pokemon_data

    def execute(self):
        session = Session(self.pokemon_data)
        session.run()
        return True


class QuitGame(GameCommand):
    def execute(self):
        return False


class GameCommandFactory:
    def __init__(self, context: 'Game'):
        self.context = context

    def create_command(self, action: MainActions):
        commands = {
            MainActions.NEW_GAME: StartNewSession(self.context.pokemon_data),
            MainActions.QUIT: QuitGame(),
        }
        return commands[action]
