from time import sleep

from .battle_menu import BattleAction


class TurnService:
    def __init__(self, context):
        self.context = context

    def player_action(self) -> bool:
        action = self.context.menu.display_menu()
        command = self.context.command_factory.create_command(action, self.context.player_pokemon,
                                                              self.context.enemy_pokemon)
        should_continue = command.execute()
        if action == BattleAction.ATTACK:
            self.context.notify(self.context.player_pokemon, self.context.enemy_pokemon)
            sleep(1)
        return should_continue

    def enemy_action(self) -> bool:
        command = self.context.command_factory.create_command(BattleAction.ATTACK, self.context.enemy_pokemon,
                                                              self.context.player_pokemon)
        should_continue = command.execute()
        self.context.notify(self.context.player_pokemon, self.context.enemy_pokemon)
        sleep(1)
        return should_continue
