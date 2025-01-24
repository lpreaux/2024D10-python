import os
import re
from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass
from typing import List

from ..core import Pokemon


@dataclass
class DisplayState:
    player_pokemon: Pokemon
    enemy_pokemon: Pokemon


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

    @staticmethod
    def strip_ansi(text):
        return re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', text)


class BattleObserver(ABC):
    @abstractmethod
    def update(self, player_pokemon: Pokemon, enemy_pokemon: Pokemon):
        pass

    def add_message(self, message):
        pass


class Box:
    TOP_LEFT = '┌'
    TOP_RIGHT = '┐'
    BOTTOM_LEFT = '└'
    BOTTOM_RIGHT = '┘'
    HORIZONTAL = '─'
    VERTICAL = '│'
    T_DOWN = '┬'
    T_UP = '┴'
    T_RIGHT = '├'
    T_LEFT = '┤'


class BattleDisplay(BattleObserver):
    def __init__(self):
        self.message_history = deque(maxlen=5)
        self.display_height = 15
        self.current_state = None
        self.width = 58  # Adjusted for better alignment
        self.box = Box()

    def update(self, player_pokemon: Pokemon, enemy_pokemon: Pokemon):
        self.current_state = DisplayState(player_pokemon, enemy_pokemon)
        self._refresh_display()

    def add_message(self, message: str):
        self.message_history.append(message)
        if self.current_state:
            self._refresh_display()

    def _refresh_display(self):
        self.clear_screen()
        print(f"\n{Colors.BOLD}⚔️  POKEMON BATTLE  ⚔️{Colors.ENDC}\n")
        self._draw_box(lambda: self.display_pokemon_info(self.current_state.enemy_pokemon, is_enemy=True))
        print()
        self._draw_separator()
        print()
        self._draw_box(lambda: self.display_pokemon_info(self.current_state.player_pokemon, is_enemy=False))
        print()
        self._draw_battle_log()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_box(self, content_fn):
        print(f"{self.box.TOP_LEFT}{self.box.HORIZONTAL * (self.width - 2)}{self.box.TOP_RIGHT}")
        content_fn()
        print(f"{self.box.BOTTOM_LEFT}{self.box.HORIZONTAL * (self.width - 2)}{self.box.BOTTOM_RIGHT}")

    def _draw_separator(self):
        print(Colors.YELLOW + '▰' * self.width + Colors.ENDC)

    def _draw_battle_log(self):
        print(f"{Colors.CYAN}{self.box.T_RIGHT}{self.box.HORIZONTAL * (self.width - 2)}{self.box.T_LEFT}")
        title = f" Battle Log "
        padding_left = (self.width - len(title) - 2) // 2
        padding_right = self.width - len(title) - 2 - padding_left
        print(
            f"{Colors.CYAN}{self.box.VERTICAL}{' ' * padding_left}{Colors.BOLD}{title}{Colors.ENDC}{Colors.CYAN}{' ' * padding_right}{self.box.VERTICAL}")
        print(f"{Colors.CYAN}{self.box.T_RIGHT}{self.box.HORIZONTAL * (self.width - 2)}{self.box.T_LEFT}{Colors.ENDC}")

        for msg in self.message_history:
            stripped_msg = Colors.strip_ansi(msg)
            padding = self.width - len(stripped_msg) - 3
            print(
                f"{Colors.CYAN}{self.box.VERTICAL}{Colors.ENDC} {msg}{' ' * padding}{Colors.CYAN}{self.box.VERTICAL}{Colors.ENDC}")

        remaining_lines = self.display_height - len(self.message_history) - 8
        for _ in range(remaining_lines):
            print(f"{Colors.CYAN}{self.box.VERTICAL}{' ' * (self.width - 2)}{self.box.VERTICAL}{Colors.ENDC}")

        print(
            f"{Colors.CYAN}{self.box.BOTTOM_LEFT}{self.box.HORIZONTAL * (self.width - 2)}{self.box.BOTTOM_RIGHT}{Colors.ENDC}")

    def display_pokemon_info(self, pokemon: Pokemon, is_enemy: bool = False):
        prefix = f"{Colors.RED}Enemy{Colors.ENDC}" if is_enemy else f"{Colors.GREEN}Your{Colors.ENDC}"
        name_display = f"{prefix} {Colors.BOLD}{pokemon.name}{Colors.ENDC} {pokemon.types}"
        stripped_name = Colors.strip_ansi(name_display)
        padding = self.width - len(stripped_name) - 3
        print(f"{self.box.VERTICAL} {name_display}{' ' * padding}{self.box.VERTICAL}")

        hp_display = f"HP: {self._generate_hp_bar(pokemon)} ({pokemon.hp}/{pokemon.max_hp})"
        stripped_hp = Colors.strip_ansi(hp_display)
        padding = self.width - len(stripped_hp) - 3
        print(f"{self.box.VERTICAL} {hp_display}{' ' * padding}{self.box.VERTICAL}")

    def _generate_hp_bar(self, pokemon: Pokemon, length: int = 20) -> str:
        hp_percentage = pokemon.hp / pokemon.max_hp
        filled = int(length * hp_percentage)
        empty = length - filled
        color = Colors.GREEN if hp_percentage > 0.5 else Colors.YELLOW if hp_percentage > 0.2 else Colors.RED
        return f"{color}[{'█' * filled}{'░' * empty}]{Colors.ENDC}"


class Subject:
    def __init__(self):
        self._observers: List[BattleObserver] = []

    def attach(self, observer: BattleObserver):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: BattleObserver):
        self._observers.remove(observer)

    def notify(self, player_pokemon: Pokemon, enemy_pokemon: Pokemon):
        for observer in self._observers:
            observer.update(player_pokemon, enemy_pokemon)

    def add_message(self, message: str):
        for observer in self._observers:
            observer.add_message(message)