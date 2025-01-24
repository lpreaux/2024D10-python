from abc import ABC, abstractmethod
from time import sleep


class BattleState(ABC):
    @abstractmethod
    def handle_state(self, context):
        pass

class StartBattle(BattleState):
    def handle_state(self, context):
        context.add_message(f"A wild {context.enemy_pokemon.name} appeared!")
        context.notify(context.player_pokemon, context.enemy_pokemon)
        sleep(1)
        context.next_state(StartTurn())

class StartTurn(BattleState):
    def handle_state(self, context):
        context.next_state(PlayerAction())

class PlayerAction(BattleState):
    def handle_state(self, context):
        context.add_message("It's your turn ! Choose what to do ...")
        sleep(0.5)
        if context.turn_service.player_action():
            context.next_state(EnemyAction())
        else:
            context.next_state(EndBattle())

class EnemyAction(BattleState):
    def handle_state(self, context):
        context.add_message("It's the enemy turn... Choosing action...")
        sleep(0.5)
        context.turn_service.enemy_action()
        context.next_state(EndTurn())

class EndTurn(BattleState):
    def handle_state(self, context):
        if context.battle_service.is_battle_over():
            context.next_state(EndBattle())
        else:
            context.next_state(StartTurn())

class EndBattle(BattleState):
    def handle_state(self, context):
        if context.enemy_pokemon.hp <= 0:
            context.add_message(f"{context.enemy_pokemon.name} is KO! {context.player_pokemon.name} wins!")
            context.add_message("You WIN!")
        elif context.player_pokemon.hp <= 0:
            context.add_message(f"{context.player_pokemon.name} is KO! {context.enemy_pokemon.name} wins!")
            context.add_message("You LOSE!")
        else:
            context.add_message(f"You fled from battle!")

        input("Appuyez sur Entrée pour continuer...")