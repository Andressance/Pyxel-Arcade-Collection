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
        
        
        self.aiManager = EnemyAI(self.x, self.y, self.health)
        self.animationManager = AiAnimationManager(
            sprite_sheet=self.sprite_sheet,
            coords={
                "idle": {"frames": [(144, 128, 0, 35, 64)], "time": 0.15, "max_frame": 0},
                "chasing": {"frames": [(24, 0, 0, 39, 64), (64, 0, 0, 39, 64), (104, 0, 0, 39, 64), (152, 0, 0, 39, 64), (192, 0, 0, 39, 64), (0, 64, 0, 56, 64)], "time": 0.15, "max_frame": 5},
                "attacking_up": {"frames": [(0, 144, 0, 64, 64), (56, 64, 0, 87, 63), (80, 128, 0, 63, 64)], "time": 0.15, "max_frame": 2},
                "attacking_down": {"frames": [(80, 128, 0, 63, 64), (56, 64, 0, 87, 63), (0, 144, 0, 64, 64)], "time": 0.15, "max_frame": 2},
                "attacking_forward": {"frames": [(0, 0, 0, 0, 0)], "time": 0.15, "max_frame": 0},
                "blocking_up": {"frames": [(0, 128, 0, 78, 79)], "time": 0.2, "max_frame": 0},
                "blocking_down": {"frames": [(80, 128, 0, 63, 64)], "time": 0.2, "max_frame": 0},
                "blocking_forward": {"frames": [(0, 128, 0, 78, 79)], "time": 0.2, "max_frame": 0}
            },
            sprite_size=64,
            state_tree=self.aiManager
        )
        self.frame_count = 0

    def update(self, player_x, player_y, player_state):
        self.x, self.y = self.aiManager.update(player_x, player_y, player_state)
        self.animationManager.update(self.x, self.y)

    def draw(self):
        self.animationManager.draw()
        