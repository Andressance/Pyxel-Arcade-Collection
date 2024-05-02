import pyxel as px
from random import randint
from .AIManager import AiAnimationManager, EnemyAI

class Enemy:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        self.MAX_HEALTH = 100

        self.sprite_x = 0
        self.sprite_y = 0
        self.sprite_size = 65
        self.hitbox = ((self.x, self.x + self.sprite_size), (self.y, self.y + self.sprite_size))
        
        self.sprite_sheet = "resources/sprites/enemy.pyxres"
        
        px.load(self.sprite_sheet)
        
        self.aiManager = EnemyAI(self.x, self.y, self.health)
        self.aimationManager= AiAnimationManager(
            sprite_sheet=self.sprite_sheet,
            idle_coords=[(0, 0, 0, 0, 0)],
            walk_coords=[(24, 0, 0, 39, 64), (64, 0, 0, 39, 64), (104, 0, 0, 39, 64), (152, 0, 0, 39, 64), (192,0,0,39,64), (0,64,0,56, 64)],
            mid_attack_coords=[(0, 0, 0, 0, 0)],
            bot_attack_coords=[(0, 0, 0, 0, 0)],
            top_attack_coords=[(0, 0, 0, 0, 0)],
            force_pushing_coords=[(0, 0, 0, 0, 0)],
            block_coords=[(0, 0, 0, 0, 0)],
            stateTree=self.aiManager
        )
        self.frame_count = 0

    def update(self, player_x, player_y, player_state):
        self.x, self.y = self.aiManager.update(player_x, player_y, player_state)
        self.aimationManager.update(self.x, self.y)

    def draw(self):
        self.aimationManager.draw(self.x, self.y, self.aiManager.distance)
        