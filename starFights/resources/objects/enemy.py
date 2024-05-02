import pyxel as px
from random import randint
from .AIManager import AIManager, AiAnimationManager

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
        
        self.aiManager = AIManager(self.x, self.y, self.health)
        self.aimationManager= AiAnimationManager()

        self.frame_count = 0
        