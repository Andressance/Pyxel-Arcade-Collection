import pyxel as px
from .stateTree import stateTree
from .animationManager import animationManager
from time import sleep

class Player:
    def __init__(self,x,y,health):
        self.x = x
        self.y = y
        self.health = health
        self.sprite_x = 0
        self.sprite_y = 0
        self.sprite_size = 65
        

        

        self.sprite_sheet = "resources/sprites/sprites.pyxres"
        px.load(self.sprite_sheet)

        self.stateTree = stateTree({
            "walking_right": px.KEY_D,
            "walking_left": px.KEY_A,
            "jumping": px.KEY_W,
            "crouching": px.KEY_S,
            "attacking": px.KEY_E,
            "blocking": px.KEY_Q,
            "blocking_down": px.KEY_Q + px.KEY_DOWN,
            "blocking_forward": px.KEY_Q + px.KEY_UP,
            "attaking_up": px.KEY_E + px.KEY_UP,
            "attacking_down": px.KEY_E + px.KEY_DOWN,
            "attacking_forward": px.KEY_E,
            }
        )

        self.animationManager = animationManager(
            self.sprite_sheet,
            [(0,0),(0,72),(0,144)],
            [(72,0),(72,72),(72,144),(144, 0)],
            None,
            [(144,64)],
            64,
            self.stateTree                        
        )

    def update(self):
        self.stateTree.update()
        self.animationManager.update()
        self.move()


    def draw(self):
        self.animationManager.draw(self.x, self.y)
        
    def move(self):
        if self.stateTree.states["walking_right"]:
            self.x += 1
        if self.stateTree.states["walking_left"]:
            self.x -= 1
        
   