from ..core import Pokemon
from .battle_state import StartBattle, EndBattle
from .battle_menu import BattleActionMenu
from .battle_command import BattleCommandFactory
from .turn_service import TurnService
from .battle_service import BattleService
from .battle_display import Subject, BattleDisplay


class Battle(Subject):
    def __init__(self, player_pokemon: Pokemon, enemy_pokemon: Pokemon):
        super().__init__()
        self._state = StartBattle()
        self.player_pokemon = player_pokemon
        self.enemy_pokemon = enemy_pokemon
        self.menu = BattleActionMenu(self)
        self.command_factory = BattleCommandFactory(self)
        self.turn_service = TurnService(self)
        self.battle_service = BattleService(self)

        self.display = BattleDisplay()
        self.attach(self.display)

    def start_battle(self):
        self.display.clear_screen()
        while self.execute_turns():
            pass
        self._state.handle_state(self)
        self.display.clear_screen()

    def execute_turns(self):
        while not isinstance(self._state, EndBattle):
            self._state.handle_state(self)

    def next_state(self, state):
        self._state = state
