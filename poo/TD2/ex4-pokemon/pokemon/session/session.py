from typing import TYPE_CHECKING

from .session_service import SessionService
from .session_state import SessionState, StartSession, EndSession

if TYPE_CHECKING:
    from ..core import Pokemon, PokemonFactory

class Session:
    def __init__(self, pokemon_data: dict):
        self.pokemon_data: dict = pokemon_data
        self._player_pokemon = None

        self._session_service: SessionService = SessionService(self, pokemon_data)

        self._state: SessionState = StartSession()

    @property
    def player_pokemon(self) -> 'Pokemon':
        return self._player_pokemon

    @player_pokemon.setter
    def player_pokemon(self, pokemon: 'Pokemon'):
        self._player_pokemon = pokemon

    def run(self):
        while not isinstance(self._state, EndSession):
            self._state.handle(self, self._session_service)
        self._state = self._state.handle(self, self._session_service)

    def next_state(self, state):
        self._state = state