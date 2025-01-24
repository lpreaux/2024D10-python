from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from session import Session
    from .session_service import SessionService


class SessionState(ABC):
    def handle(self, context: "Session", service: "SessionService"):
        pass

class StartSession(SessionState):
    def handle(self, context: "Session", service: "SessionService"):
        if service.is_new_session():
            context.next_state(InitNewSession())
        else:
            context.next_state(LoadExistingSession())

class InitNewSession(SessionState):
    def handle(self, context: "Session", service: "SessionService"):
        service.init_session()
        context.next_state(Battle())

class LoadExistingSession(SessionState):
    def handle(self, context: "Session", service: "SessionService"):
        pass

class Battle(SessionState):
    def handle(self, context: "Session", service: "SessionService"):
        service.do_battle()
        if context.player_pokemon.hp <= 0:
            context.next_state(EndSession())
        else:
            context.next_state(Battle())

class EndSession(SessionState):
    def handle(self, context: "Session", service: "SessionService"):
        print("Your pokemon is dead!")
        print("You LOSE!")