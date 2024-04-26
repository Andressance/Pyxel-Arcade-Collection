import pyxel as px
from time import sleep
class stateTree:
    def __init__(self, movement_keys: dict, pressed_keys):
        # Creamos un diccionario con todos los posibles estados del jugador y los inicializamos como False
        self.states = {
            "idle": True, 
            "walking_right": False, 
            "walking_left": False, 
            "crouching": False, 
            "blocking": False, 
            "blocking_up": False, 
            "blocking_down": False
        }

        self.pressed_states = {
            "jumping": False, 
            "attacking_up": False, 
            "attacking_down": False, 
            "attacking_forward": False,
            # "dodging_up": False, 
            # "dodging_down": False, 
            # "dodging_forward": False, 
            # "dodging_backward": False, 
        }
        self.movement_keys = movement_keys
        self.pressed_keys = pressed_keys

        self.frame_count = 0
        self.on_animation = False
        self.before_state = None
        

    def update(self):

        
        self.before_state = self.get_current_state()

        if not self.on_animation:
            
            self.states = {state: False if state != "idle" else True for state in self.states}
            self.pressed_states = {state: False for state in self.pressed_states}

            for state, key in self.movement_keys.items():
                if px.btn(key):
                    self.states[state] = True
                    self.states["idle"] = False
                    

            for state, key in self.pressed_keys.items():
                if px.btnp(key):
                    self.pressed_states[state] = True
                    self.states["idle"] = False
                    self.on_animation = True
                    
                    
        else:
            self.frame_count += 1
            if self.frame_count > 35:
                self.on_animation = False
                self.frame_count = 0
                
                

    

    def get_current_state(self):
        for state, value in self.states.items():
            if value:
                return state

        for state, value in self.pressed_states.items():
            if value:
                return state
    
    