import pyxel as px
from .stateTree import stateTree
from .animationManager import animationManager
from time import sleep
from .playerHUD import PlayerHUD
from random import randint
from . import staminaManager, forceManager

class Player:
    def __init__(self,x,y,health):
        # Player coordinates
        self.x = x
        self.y = y

        self.frame_count = 0
        
        # Player stats
        self.health = health
        self.MAX_HEALTH = 100
        self.force = 20
        self.MAX_FORCE = 100
        self.stamina = 100
        self.MAX_STAMINA = 100
        
        
        # Draw variables
        self.sprite_x = 0
        self.sprite_y = 0
        self.sprite_size = 65

        self.distanceX = 0
        self.distanceY = 0
        
        # We create the hitbox
        self.hitbox = ((self.x,self.x + self.sprite_size),(self.y, self.y + self.sprite_size))

        # We create the HUD of player stats
        self.HUD = PlayerHUD(self.health, self.force, self.stamina, self.MAX_HEALTH, self.MAX_FORCE, self.MAX_STAMINA)
        

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
                "force_pushing": px.KEY_E
            },
            self.stamina,
            self.force
        )
        # The stateTree is a dictionary that holds the keys that are being pressed and the keys that are pressed
        # The keys that are being pressed are the keys that are  being held
        # The keys that are pressed are the keys that are pressed once

        # We create the stamina manager
        self.staminaManager = staminaManager.StaminaManager(self.stamina, self.MAX_STAMINA, self.stateTree)
        self.forceManager = forceManager.ForceManager(self.force, self.MAX_FORCE)

        self.animationManager = animationManager(
            sprite_sheet=self.sprite_sheet,
            idle_coords=[(0,0,1),(0,72,1),(0,144,1)],
            walk_coords=[(72,0,1),(72,72,1),(72,144,1),(144, 0,1)],
            mid_attack_coords=[(144,128,1),(72,0,2), (0,128,2)],
            bot_attack_coords=[(144,128,1),(0,0,2),(8,64,2)],
            top_attack_coords=[(144,128,1),(0,192,2),(0,128,2)],
            force_pushing_coords=[(72,64,2),(72,128,2)],
            block_coords=[(144,64,1)],
            sprite_size=64,
            stateTree=self.stateTree                     
        )

    def update(self, enemy_x, enemy_y):

        self.distanceX = self.x - enemy_x
        self.distanceY = self.y - enemy_y

        self.stateTree.update(self.stamina, self.force)
        self.animationManager.update(self.distanceX, self.distanceY)
        self.move()
        self.check_out_of_bounds(0, px.width - self.sprite_size)
        self.HUD.update(self.health, self.force, self.stamina)
        self.stamina = self.staminaManager.update(self.stamina, self.stateTree)
        self.force = self.forceManager.update(self.force)
        # Tests
        
        if px.btnp(px.KEY_E):
            if self.force > 20:
                self.force -= 20
            

    def draw(self):
        self.animationManager.draw(self.x, self.y)
        self.HUD.draw()
        
    def move(self):
        if self.stateTree.states["walking_right"]:
            self.x += 1
        if self.stateTree.states["walking_left"]:
            self.x -= 1
        
    def check_out_of_bounds(self, x_offset:int, y_offset:int):
        if self.x < x_offset:
            self.x = x_offset
        if self.x > y_offset:
            self.x = y_offset

    
            
        
    
            

        