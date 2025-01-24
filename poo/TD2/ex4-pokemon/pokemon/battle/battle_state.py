from abc import ABC, abstractmethod
from time import sleep


class BattleState(ABC):
    @abstractmethod
    def handle_turn(self, context):
        pass

class StartTurn(BattleState):
    def handle_turn(self, context):
        # Logique de debut de tour
        context.add_message("New turn...")
        sleep(1)
        context.notify(context.player_pokemon, context.enemy_pokemon)
        context.next_state(PlayerAction())
        return True

class PlayerAction(BattleState):
    def handle_turn(self, context):
        # Logique action joueur
        context.add_message("It's your turn...")
        sleep(1)
        context.next_state(EnemyAction())
        return context.turn_service.player_action()

class EnemyAction(BattleState):
    def handle_turn(self, context):
        # Logique action Enemy
        context.add_message("It's the enemy turn... Choosing action...")
        sleep(1)
        context.next_state(EndTurn())
        return context.turn_service.enemy_action()

class EndTurn(BattleState):
    def handle_turn(self, context):
        # Logique de fin de tour
        sleep(2)
        context.next_state(StartTurn())
        return True
