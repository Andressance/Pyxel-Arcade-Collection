import pyxel as px

class StateTree:
    def __init__(self, movement_keys: dict, pressed_keys, stamina: int, force: int):
        self.stamina = stamina
        self.force = force

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
        }

        self.movement_keys = movement_keys
        self.pressed_keys = pressed_keys

        self.frame_count = 0
        self.on_animation = False
        self.before_state = None

    def update(self, stamina: int, force: int):
        self.stamina = stamina
        self.force = force

        self.before_state = self.get_current_state()

        if not self.on_animation:
            self.frame_count = 0
            self.states = {state: False if state != "idle" else True for state in self.states}
            self.pressed_states = {state: False for state in self.pressed_states}

            for state, key in self.movement_keys.items():
                if px.btn(key):
                    self.states[state] = True
                    self.states["idle"] = False

            for state, key in self.pressed_keys.items():
                if px.btnp(key) and ((self.force >= 20 and state == "force_pushing") or (self.stamina >= 20 and state != "force_pushing")):
                    self.pressed_states[state] = True
                    self.states["idle"] = False
                    self.on_animation = True

        else:
            self.states = {state: False for state in self.states}
            self.frame_count += 1

            for state in ["attacking_forward", "attacking_down", "attacking_up", "force_pushing"]:
                if self.pressed_states[state] and self.frame_count > (30 if "attacking" in state else 25):
                    self.on_animation = False
                    self.frame_count = 0
                    self.pressed_states[state] = False

    def get_current_state(self):
        for state, value in self.states.items():
            if value:
                return state

        for state, value in self.pressed_states.items():
            if value:
                return state

        return "idle"  # Devolver estado predeterminado si no se encuentra ningún estado activo


    def is_attacking(self):
        return any([self.pressed_states[state] for state in self.pressed_states])