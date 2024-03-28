import pyxel as px
from .stateTree import stateTree
from time import sleep

class Player:
    def __init__(self,x,y,health):
        self.x = x
        self.y = y
        self.health = health
        self.sprite_x = 0
        self.sprite_y = 0
        self.sprite_size = 65
        self.frame = 0  # Animation frame
        self.frame_count = 0  # Frame counter
        self.reverse_animation = False  # Animation direction

        self.COL_IGNORE = 8 # Color to ignore when drawing sprite
        self.SEC_LIMIT = 60 # Game limited to 60 frames per second
        self.SPRITE = 1 # Image on the sprite sheet

        self.sprite_sheet = "resources/sprites/sprites.pyxres"
        px.load(self.sprite_sheet)

        self.stateTree = stateTree( {
            "walking_right": px.KEY_D,
            "walking_left": px.KEY_A,
            "jumping": px.KEY_W,
            "crouching": px.KEY_S
            }
        )

    def update(self):
        self.stateTree.update()
        self.move()
        self.animate_idle()
        
    def move(self):
        if self.stateTree.states["walking_right"]:
            self.x += 1
        if self.stateTree.states["walking_left"]:
            self.x -= 1
        if self.stateTree.states["jumping"]:
            self.y -= 1
        


    def animate_idle(self):
        if self.stateTree.states["idle"]:
            # Increment the frame counter
            self.frame_count += 1

                


            if self.frame_count > int(self.SEC_LIMIT * 0.75):  # At 0.75 seconds, change frame of the animation
                
                if self.frame == 2:  # Check if the frame is 3
                    self.reverse_animation = True  # Set the animation to reverse
                elif self.frame == 0:  # If the frame is 0
                    self.reverse_animation = False  # Set the animation to forward
                # Move the frame based on the animation direction
                
                if not self.reverse_animation:
                    self.frame += 1
                
                else:
                    self.frame -= 1

                self.frame_count = 0

            

                
            


    def draw(self):
        if self.stateTree.states["idle"]:
            px.blt(self.x, self.y, self.SPRITE, 0, (self.frame * self.sprite_size) + (7 * self.frame) - 1, self.sprite_size -1 , self.sprite_size , self.COL_IGNORE)
