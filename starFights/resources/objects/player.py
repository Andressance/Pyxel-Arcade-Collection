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

        self.stateTree = stateTree({ # Holded Keys
            "walking_right": px.KEY_D,
            "walking_left": px.KEY_A,
            "crouching": px.KEY_S,
            "blocking": px.KEY_Q,
            "blocking_down": px.KEY_S,
            "blocking_forward": px.KEY_P,
            },

            { # Pressed Keys
                "attacking_up": px.KEY_UP,
                "attacking_down": px.KEY_DOWN,
                "attacking_forward": px.KEY_RIGHT,
            }
        )

        self.animationManager = animationManager(
            sprite_sheet=self.sprite_sheet,
            idle_coords=[(0,0,1),(0,72,1),(0,144,1)],
            walk_coords=[(72,0,1),(72,72,1),(72,144,1),(144, 0,1)],
            mid_attack_coords=[(144,128,1),(72,0,2), (0,128,2)],
            bot_attack_coords=[(144,128,1),(0,0,2),(8,64,2)],
            top_attack_coords=[(144,128,1),(0,192,2),(0,128,2)],
            block_coords=[(144,64,1)],
            sprite_size=64,
            stateTree=self.stateTree                     
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
        
   