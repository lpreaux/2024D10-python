
class BattleService:
    def __init__(self, context):
        self.context = context

    def is_battle_over(self):
        return self.context.player_pokemon.hp <= 0 or self.context.enemy_pokemon.hp <= 0
