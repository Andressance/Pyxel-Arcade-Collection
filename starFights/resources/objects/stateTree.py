import pyxel as px
from time import sleep
class stateTree:
    def __init__(self, movement_keys: dict, pressed_keys, stamina: int, force: int):
        
        self.stamina = stamina
        self.force = force

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
            "attacking_up": False, 
            "attacking_down": False, 
            "attacking_forward": False,
            "force_pushing": False
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
        

    def update(self, stamina:int, force:int):

        self.stamina = stamina
        self.force = force

        # Get the current state of the player
        self.before_state = self.get_current_state()
        
        # If the player is not on an animation
        if not self.on_animation:

            self.frame_count = 0
            self.states = {state: False if state != "idle" else True for state in self.states}
            self.pressed_states = {state: False for state in self.pressed_states}

            for state, key in self.movement_keys.items():
                if px.btn(key):
                    self.states[state] = True
                    self.states["idle"] = False
                    

            for state, key in self.pressed_keys.items():
                if px.btnp(key):
                    if self.force >= 20 and state == "force_pushing":
                        self.pressed_states[state] = True
                        self.states["idle"] = False
                        self.on_animation = True
                    elif self.stamina >= 20 and state != "force_pushing":
                        self.pressed_states[state] = True
                        self.states["idle"] = False
                        self.on_animation = True
                    else:
                        pass
                    
                    
        # If the player is on an animation       
        else:
            
            self.states = {state: False for state in self.states}
            self.frame_count += 1
            
            if self.pressed_states["attacking_forward"] and self.frame_count > 30:
                self.on_animation = False
                self.frame_count = 0
                self.pressed_states["attacking_forward"] = False
                

            elif self.pressed_states["attacking_down"] and self.frame_count > 30:
                self.on_animation = False
                self.frame_count = 0
                self.pressed_states["attacking_down"] = False
                

            elif self.pressed_states["attacking_up"] and self.frame_count > 30:
                self.on_animation = False
                self.frame_count = 0
                self.pressed_states["attacking_up"] = False
            

            elif self.pressed_states["force_pushing"] and self.frame_count > 25:
                self.on_animation = False
                self.frame_count = 0
                self.pressed_states["force_pushing"] = False
                
                
                
                

    

    def get_current_state(self):
        for state, value in self.states.items():
            if value:
                return state

        for state, value in self.pressed_states.items():
            if value:
                return state
    
    def is_attacking(self):
        return self.pressed_states["attacking_up"] or self.pressed_states["attacking_down"] or self.pressed_states["attacking_forward"]
    