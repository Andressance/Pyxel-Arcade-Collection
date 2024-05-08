import pyxel as px
from .stateTree import StateTree

class AnimationManager:
    def __init__(self, sprite_sheet:str, coords: dict, sprite_size:list, state_tree:StateTree):
        self.sprite_sheet = sprite_sheet
        self.SPRITE_SIZE = sprite_size
        self.coords = coords
        self.state_tree = state_tree
        
        self.frame = 0
        self.frame_count = 0
        self.reverse_animation = False
        
        self.distanceX = 0
        self.distanceY = 0

        self.COL_IGNORE = 8
        self.SEC_LIMIT = 60
        px.load(self.sprite_sheet)

    def update(self, distanceX, distanceY):
        
        self.distanceX = distanceX
        self.distanceY = distanceY

        for action, pressed in self.state_tree.pressed_states.items():
            if pressed:
                self.animate(action)

        for action, active in self.state_tree.states.items():
            if active:
                self.animate(action)

    def animate(self, action):
        
        self.frame_count += 1

        if self.state_tree.before_state != action:
            self.frame = 0
            self.frame_count = 0

        action_coords = self.coords.get(action)
        if not action_coords:
            return

        time = action_coords.get('time', 0.12)
        if self.frame_count > int(self.SEC_LIMIT * time):
            self.frame += 1
            max_frame = action_coords.get('max_frame', 2)
            if self.frame > max_frame:
                self.frame = 0
            self.frame_count = 0

    def draw(self, characterX, characterY):
        action = self.state_tree.get_current_state()
        action_coords = self.coords.get(action)
        if not action_coords:
            return
        
        try:
            image_x, image_y, n_image = action_coords.get('frames', [None, None, None])[self.frame]
        except IndexError:
            self.frame = 0
            image_x, image_y, n_image = action_coords.get('frames', [None, None, None])[self.frame]

        if image_x is None or image_y is None or n_image is None:
            return

        if self.distanceX < 0:
            px.blt(characterX, characterY, n_image, image_x, image_y, self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)
        else:
            px.blt(characterX + self.SPRITE_SIZE, characterY, n_image, image_x, image_y, -self.SPRITE_SIZE, self.SPRITE_SIZE, self.COL_IGNORE)

