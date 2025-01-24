from ..core import Pokemon
from .battle_state import StartTurn
from .battle_menu import BattleActionMenu
from .battle_command import BattleCommandFactory
from .turn_service import TurnService
from .battle_display import Subject, BattleDisplay


class Battle(Subject):
    def __init__(self, player_pokemon: Pokemon, enemy_pokemon: Pokemon):
        super().__init__()
        self.__state = StartTurn()
        self.player_pokemon = player_pokemon
        self.enemy_pokemon = enemy_pokemon
        self.menu = BattleActionMenu(self)
        self.command_factory = BattleCommandFactory(self)
        self.turn_service = TurnService(self)

        self.display = BattleDisplay()
        self.attach(self.display)

    def start_battle(self):
        self.add_message(f"A wild {self.enemy_pokemon.name} appeared!")
        while self.execute_turn():
            pass
        self.display.clear_screen()

    def execute_turn(self):
        should_continue = self.__state.handle_turn(self)
        return should_continue and self.player_pokemon.hp > 0 and self.enemy_pokemon.hp > 0

    def next_state(self, state):
        self.__state = state
