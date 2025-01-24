from abc import ABC, abstractmethod


class GameState(ABC):
    @abstractmethod
    def handle_state(self, context):
        pass

class StartGame(GameState):
    def handle_state(self, context):
        if context.game_service.should_game_init():
            context.next_state(InitialSetup())
        else:
            context.next_state(PlayerAction())

class InitialSetup(GameState):
    def handle_state(self, context):
        context.game_service.initialize()
        context.next_state(PlayerAction())

class PlayerAction(GameState):
    def handle_state(self, context):
        if context.game_service.handle_player_action():
            context.next_state(PlayerAction())
        else:
            context.next_state(EndGame())

class EndGame(GameState):
    def handle_state(self, context):
        pass