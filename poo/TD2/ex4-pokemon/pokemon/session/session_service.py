import random
from time import sleep
from typing import TYPE_CHECKING

from ..battle import Battle
from ..core import PokemonFactory

if TYPE_CHECKING:
    from .session import Session

class SessionService:
    def __init__(self, context: 'Session', pokemon_data: dict):
        self.context = context
        self.pokemon_data = pokemon_data

    def is_new_session(self):
       return True

    def init_session(self):
        print("Welcome to this new adventure!")
        sleep(1.5)
        name = input("What's your name? ")
        self.context.player_name = name
        print(f"Ah, {name}! What a wonderful name for a future champion!")
        sleep(1)
        print(f"Listen closely, {name}, for you're about to enter a magnificent world!")
        sleep(1.5)
        print("A world where mystical creatures roam. They're called Pokémon!")
        sleep(1)
        print("Starting today, you'll have your own Pokémon! And you'll fight!")
        sleep(0.8)
        print("YOU'LL FIGHT!")
        sleep(0.3)
        print("FIGHT! FIGHT! FIGHT!")
        sleep(0.8)
        print("Fight until your Pokémon died, and then start all over again!")
        sleep(1)
        print("Every single time they died!")
        sleep(0.8)
        print("You'll fight for your life! You'll fight for glory!")
        sleep(1)
        print("You'll fight for your fans...")
        sleep(1.5)
        print("Oh wait... ")
        sleep(1)
        print("You're all alone.")
        sleep(2)
        print("But nonetheless! You'll Fight!")
        sleep(0.5)
        print("Fight! Fight! Fight!")
        sleep(0.3)
        print("FIIIIIIIGHT!")
        sleep(1)
        print("...")
        sleep(1)
        print("*coughs*")
        sleep(1)
        print("Excuse my enthusiasm...")
        sleep(1.5)
        print("Now then, every trainer needs their first Pokémon.")
        sleep(1)
        print("And I have just the one for you!")
        sleep(0.8)
        print("See how nice I am?")
        sleep(1)
        print(
            "*muttering to himself* Yes, I'm nice! It's not at all because I live for battle and want to see you fight...")
        sleep(2)
        print("Huh? You could hear me? Oh... well... my apologies!")
        sleep(1)
        print("So... where were we?")
        sleep(1)
        print("Ah yes, your first Pokémon!")
        sleep(0.8)
        print("Pikachu! Come forth!")
        sleep(0.5)
        print("*throwing a ball*")
        sleep(0.5)
        print("Pika! Pikaa!")
        sleep(1)
        print("Behold! Here's Pikachu, your very first companion!")
        sleep(1.5)
        print("Now, step through that door and begin your journey!")
        sleep(1)
        print("Step through that door and start to FIGHT!")
        sleep(1)
        self.context.player_pokemon = PokemonFactory.create_pokemon("Pikachu", self.context.pokemon_data)

    def do_battle(self):
        random_pokemon_name = random.choice(list(self.pokemon_data.keys()))
        enemy_pokemon = PokemonFactory.create_pokemon(random_pokemon_name, self.context.pokemon_data)

        battle = Battle(self.context.player_pokemon, enemy_pokemon)
        battle.start_battle()