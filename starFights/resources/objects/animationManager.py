import pyxel as px
from .stateTree import stateTree

class animationManager:
    def __init__(self, sprite_sheet:str,  idle_coords, walk_coords, attack_coords, block_coords, sprite_size,stateTree:stateTree):
        self.sprite_sheet = sprite_sheet
        self.SPRITE_SIZE = sprite_size
        self.idle_coords = idle_coords
        self.walk_coords = walk_coords
        self.attack_coords = attack_coords
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
    
    def animate_idle(self):
        # Increment the frame counter
        self.frame_count += 1

            
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


    def draw(self, characterX , characterY):
        
        state = self.stateTree.get_current_state()

        # Get the coordinates of the sprite based on the state of the player
        if state == "idle":
            try:
                image_x, image_y = self.idle_coords[self.frame]
            except IndexError:
                image_x, image_y = self.idle_coords[0]
                self.frame = 0
                self.frame_count = 0
        elif state == "walking_right" or state == "walking_left":
            try:
                image_x, image_y = self.walk_coords[self.frame]
            except IndexError:
                image_x, image_y = self.walk_coords[0]
                self.frame = 0
                self.frame_count = 0
        elif state == "blocking":
            try:
                image_x, image_y = self.block_coords[0]
            except IndexError:
                image_x, image_y = self.block_coords[0]
                self.frame = 0
                self.frame_count = 0

        # Draw the sprite based on the state of the player
        if self.stateTree.states["idle"]:
            px.blt(characterX, characterY, 1, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)

        elif self.stateTree.states["walking_right"] or self.stateTree.states["walking_left"]:
            px.blt(characterX, characterY, 1, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)

        elif self.stateTree.states["blocking"]:
            try:
                image_x, image_y = self.block_coords[0]
            except IndexError:
                image_x, image_y = self.block_coords[0]
            px.blt(characterX, characterY, 1, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)


    

