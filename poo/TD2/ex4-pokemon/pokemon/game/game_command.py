from abc import abstractmethod

from .game_menu import MainActions


class GameCommand:
    @abstractmethod
    def execute(self):
        pass

class StartNewSession(GameCommand):
    def execute(self):
        return True


class QuitGame(GameCommand):
    def execute(self):
        return False

class GameCommandFactory:
    def create_command(self, action: MainActions):
        commands = {
            MainActions.NEW_GAME: StartNewSession(),
            MainActions.QUIT: QuitGame(),
        }
        return commands[action]
