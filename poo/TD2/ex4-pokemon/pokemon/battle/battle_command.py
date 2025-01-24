from abc import ABC, abstractmethod
from time import sleep
from typing import Optional, Dict

from ..core import Pokemon
from .battle_menu import BattleAction

class BattleCommand(ABC):
    @abstractmethod
    def execute(self) -> bool:
        pass

class AttackCommand(BattleCommand):
    def __init__(self, context, attacker: Pokemon, defender: Pokemon):
        self.context = context
        self.attacker = attacker
        self.defender = defender

    def execute(self) -> bool:
        self.context.add_message(f"{self.attacker.name} attack !")
        sleep(1)
        self.attacker.attack(self.defender)
        return self.defender.hp > 0

class FleeCommand(BattleCommand):
    def __init__(self, context):
        self.context = context

    def execute(self) -> bool:
        self.context.add_message("You try to flee")
        return False


class BattleCommandFactory:
    def __init__(self, context):
        self.context = context

    def create_command(self, action: BattleAction, attacker: Optional[Pokemon] = None, defender: Optional[Pokemon] = None) -> BattleCommand:
        commands: Dict[BattleAction, BattleCommand] = {
            BattleAction.ATTACK: AttackCommand(self.context, attacker, defender),
            BattleAction.FLEE: FleeCommand(self.context),
        }
        return commands[action]