from enum import Enum


class MainActions(Enum):
    NEW_GAME = 'Start a new game'
    QUIT = 'Quit'


class GameMenu:
    def display_menu(self):
        print("What would you like to do?")
        for idx, action in enumerate(MainActions):
            print(f"{idx + 1} - {action.value}")
        try:
            choice = int(input("Enter your choice (1-2): "))
            if choice == 1:
                return MainActions.NEW_GAME
            elif choice == 2:
                return MainActions.QUIT
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
