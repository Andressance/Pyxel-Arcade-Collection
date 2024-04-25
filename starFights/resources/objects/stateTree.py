import pyxel as px

class stateTree:
    def __init__(self, movement_keys: dict):
        # Creamos un diccionario con todos los posibles estados del jugador y los inicializamos como False
        self.states = {
            "idle": True, 
            "walking_right": False, 
            "walking_left": False, 
            "jumping": False, 
            "falling": False, 
            "attacking_up": False, 
            "attacking_down": False, 
            "attacking_forward": False,
            "crouching": False, 
            "dodging_up": False, 
            "dodging_down": False, 
            "dodging_forward": False, 
            "dodging_backward": False, 
            "blocking": False, 
            "blocking_up": False, 
            "blocking_down": False
        }
        self.movement_keys = movement_keys

    def update(self):

        # Establecer todos los estados en False inicialmente
        self.states = {state: False if state != "idle" else True for state in self.states}

        # Actualizar los estados según las teclas presionadas
        for state, key in self.movement_keys.items():
            if px.btn(key):
                self.states[state] = True
                self.states["idle"] = False

    def get_current_state(self):
        return [state for state, value in self.states.items() if value][0]