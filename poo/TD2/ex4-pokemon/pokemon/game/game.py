from .game_state import GameState, StartGame, EndGame
from .game_menu import GameMenu
from .game_service import GameService
from .game_command import GameCommandFactory


class Game:
    def __init__(self):
        self._state: GameState = StartGame()
        self._menu: GameMenu = GameMenu()
        self._command_factory = GameCommandFactory()

        self._game_service: GameService = GameService(self)

    @property
    def state(self) -> GameState:
        return self._state

    @property
    def menu(self) -> GameMenu:
        return self._menu

    @property
    def command_factory(self) -> GameCommandFactory:
        return self._command_factory

    @property
    def game_service(self) -> GameService:
        return self._game_service

    def start_game(self) -> None:
        self.execute_game()
        self._state.handle_state(self)

    def execute_game(self):
        while not isinstance(self._state, EndGame):
            self._state.handle_state(self)

    def next_state(self, state):
        self._state = state