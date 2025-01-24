from enum import Enum


class BattleActions(Enum):
    ATTACK = 'attack'
    FLEE = 'flee'

class BattleActionMenu:
    def __init__(self, context):
        self.context = context

    def display_menu(self)-> BattleActions:
        while True:
            self.context.add_message("What would you like to do?")
            self.context.add_message("1. Attack")
            self.context.add_message("2. Flee")
            try:
                choice = int(input("Enter your choice (1-2): "))
                if choice == 1:
                    return BattleActions.ATTACK
                elif choice == 2:
                    return BattleActions.FLEE
            except ValueError:
                self.context.add_message("Invalid input. Please enter 1 or 2.")