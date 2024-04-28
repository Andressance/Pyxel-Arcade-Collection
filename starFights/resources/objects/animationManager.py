import pyxel as px
from .stateTree import stateTree

class animationManager:
    def __init__(self, sprite_sheet:str,  idle_coords:list, walk_coords:list, mid_attack_coords:list, 
                 bot_attack_coords:list, top_attack_coords:list, force_pushing_coords:list, block_coords:list, sprite_size:list, stateTree:stateTree):
        self.sprite_sheet = sprite_sheet
        self.SPRITE_SIZE = sprite_size
        self.idle_coords = idle_coords
        self.walk_coords = walk_coords
        self.mid_attack_coords = mid_attack_coords
        self.bot_attack_coords = bot_attack_coords
        self.top_attack_coords = top_attack_coords
        self.force_pushing_coords = force_pushing_coords
        self.block_coords = block_coords
        self.stateTree = stateTree # Character state tree

        self.frame = 0  # Animation frame
        self.frame_count = 0  # Frame counter
        self.reverse_animation = False  # Animation direction
        

        self.COL_IGNORE = 8 # Color to ignore when drawing sprite
        self.SEC_LIMIT = 60 # Game limited to 60 frames per second

        
        px.load(self.sprite_sheet)


    def update(self):
        
        if self.stateTree.states["idle"]:
            self.animate_idle()
        elif self.stateTree.states["walking_right"] or self.stateTree.states["walking_left"]:
            self.animate_walk()
        elif self.stateTree.states["blocking"]:
            pass
        elif self.stateTree.pressed_states["attacking_forward"]:
            self.animate_mid_attack()
        elif self.stateTree.pressed_states["attacking_down"]:
            self.animate_bot_attack()
        elif self.stateTree.pressed_states["attacking_up"]:
            self.animate_top_attack()
        elif self.stateTree.pressed_states["force_pushing"]:
            self.animate_force_pushing()
    
    def animate_idle(self):
        # Increment the frame counter
        self.frame_count += 1

        if self.stateTree.before_state != "idle":   
            self.frame = 0
            self.frame_count = 0

        if self.frame_count > int(self.SEC_LIMIT * 0.5):  # At 0.75 seconds, change frame of the animation
            
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

            

    def animate_walk(self):
        self.frame_count += 1
        
        if self.stateTree.before_state != "walking_right" and self.stateTree.before_state != "walking_left":
            self.frame = 0
            self.frame_count = 0

        if self.frame_count > int(self.SEC_LIMIT * 0.15):
            # At 0.15 seconds, change frame of the animation
            if self.stateTree.states["walking_right"]:
                # Si el jugador está caminando hacia la derecha, aumenta el frame
                if self.frame >= 3:
                    self.frame = 0
                else:
                    self.frame += 1
            elif self.stateTree.states["walking_left"]:
                # Si el jugador está caminando hacia la izquierda, disminuye el frame
                if self.frame <= 0:
                    self.frame = 3
                else:
                    self.frame -= 1

            self.frame_count = 0

    def animate_mid_attack(self):
        
        self.frame_count += 1
        
        if self.stateTree.before_state != "attacking_forward":
            self.frame = 0
            self.frame_count = 0

        if self.frame_count > int(self.SEC_LIMIT * 0.12):
            # At 0.15 seconds, change frame of the animation
            self.frame += 1
            if self.frame >= 3:
                self.frame = 0
            
            self.frame_count = 0

    def animate_bot_attack(self):
        
        self.frame_count += 1
        
        if self.stateTree.before_state != "attacking_down":
            self.frame = 0
            self.frame_count = 0

        if self.frame_count > int(self.SEC_LIMIT * 0.12):
            # At 0.15 seconds, change frame of the animation
            self.frame += 1
            if self.frame > 2:
                self.frame = 0
            
            self.frame_count = 0

    def animate_top_attack(self):
            
            self.frame_count += 1
            
            
            if self.stateTree.before_state != "attacking_up":
                self.frame = 0
                self.frame_count = 0
    
            if self.frame_count > int(self.SEC_LIMIT * 0.12):
                # At 0.15 seconds, change frame of the animation
                self.frame += 1
                if self.frame > 2:
                    self.frame = 0
                
                self.frame_count = 0

    def animate_force_pushing(self):
            
            self.frame_count += 1
            time = 0.1 if self.frame == 0 else 0.25
            if self.stateTree.before_state != "force_pushing":
                self.frame = 0
                self.frame_count = 0
    
            if self.frame_count > int(self.SEC_LIMIT * time):
                # At 0.12 seconds, change frame of the animation
                self.frame += 1
                if self.frame > 1:
                    self.frame = 0
                
                self.frame_count = 0
        


    def draw(self, characterX , characterY):
            

        # Draw the sprite based on the state of the player
        if self.stateTree.states["idle"]:
            
            image_x, image_y, n_image = self.idle_coords[self.frame]

            px.blt(characterX, characterY, n_image, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)

        elif self.stateTree.states["walking_right"] or self.stateTree.states["walking_left"]:
            
            image_x, image_y, n_image = self.walk_coords[self.frame]
            
            px.blt(characterX, characterY, n_image, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)

        elif self.stateTree.states["blocking"]:
            
            image_x, image_y, n_image = self.block_coords[0]
            
            px.blt(characterX, characterY, n_image, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)

        elif self.stateTree.pressed_states["attacking_forward"]:
            
            image_x, image_y, n_image = self.mid_attack_coords[self.frame]
            
            px.blt(characterX, characterY, n_image, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)

        elif self.stateTree.pressed_states["attacking_down"]:
            
            image_x, image_y, n_image = self.bot_attack_coords[self.frame]
            
            px.blt(characterX, characterY, n_image, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)

        elif self.stateTree.pressed_states["attacking_up"]:
            
            image_x, image_y, n_image = self.top_attack_coords[self.frame]
            
            px.blt(characterX, characterY, n_image, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)

        elif self.stateTree.pressed_states["force_pushing"]:

            image_x, image_y, n_image = self.force_pushing_coords[self.frame]
            
            px.blt(characterX, characterY, n_image, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)
    

