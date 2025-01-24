
class GameService:
    def __init__(self, context):
        self.context = context

    def should_game_init(self) -> bool:
        return True

    def initialize(self):
        pass

    def handle_player_action(self):
        action = self.context.menu.display_menu()
        command =  self.context.command_factory.create_command(action)
        return command.execute()
