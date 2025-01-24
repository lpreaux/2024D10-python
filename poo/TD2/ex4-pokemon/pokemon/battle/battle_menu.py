from enum import Enum


class BattleAction(Enum):
    ATTACK = 'attack'
    FLEE = 'flee'

class BattleActionMenu:
    def __init__(self, context):
        self.context = context

    def display_menu(self)-> BattleAction:
        while True:
            self.context.add_message("What would you like to do?")
            self.context.add_message("1. Attack")
            self.context.add_message("2. Flee")
            try:
                choice = int(input("Enter your choice (1-2): "))
                if choice == 1:
                    return BattleAction.ATTACK
                elif choice == 2:
                    return BattleAction.FLEE
            except ValueError:
                self.context.add_message("Invalid input. Please enter 1 or 2.")