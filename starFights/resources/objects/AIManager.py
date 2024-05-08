import random
import pyxel as px

class EnemyAI:
    def __init__(self, enemy_x, enemy_y, enemy_health):
        self.enemy_x, self.enemy_y = enemy_x, enemy_y
        self.enemy_health = enemy_health
        
        self.states = {
            "idle": True,
            "chasing": False,
            "blocking_up": False,
            "blocking_down": False,
            "blocking_forward": False
        }

        self.animation_states = {
            "attacking_up": False,
            "attacking_down": False,
            "attacking_forward": False,
            "pushed": False
        }

        self.before_state = "idle"
        self.distance = 0
        self.attack_cooldown = 0

        self.in_animation = False
        self.frame_count = 0

    def update(self, player_x, player_y, player_state):
        self.enemy_x, self.enemy_y = self.update_states(player_x, player_y, player_state)
        print(self.before_state)

        if self.states["chasing"]:
            self.chase_player(player_x)
        elif self.animation_states["pushed"]:
            self.pushed()

        return self.enemy_x, self.enemy_y

    def update_states(self, player_x, player_y, player_state):
        self.before_state = self.get_current_state()
        self.distance = self.enemy_x - player_x 


        if self.enemy_health <= 0:
                self.states["idle"] = True
                self.states["chasing"] = False
                self.states["blocking_up"] = False
                self.states["blocking_down"] = False
                self.states["blocking_forward"] = False
               



        if self.in_animation:
            self.frame_count += 1
            if self.frame_count > 20:
                self.in_animation = False
                if self.get_current_state() in ["attacking_up", "attacking_down", "attacking_forward"]:
                    self.attack_cooldown = 60
                self.reset_animation()
        else:
            

            if abs(self.distance) > 45:
                self.states["chasing"] = True
                self.states["idle"] = False

            else:
                self.states["chasing"] = False
                self.states["idle"] = True

                if player_state == "force_pushing":
                    self.animation_states["pushed"] = True
                    self.in_animation = True
                   
                if self.attack_cooldown > 0:
                    self.attack_cooldown -= 1
                    if self.attack_cooldown < 0:
                        self.attack_cooldown = 0

                # Block
                if player_state in ["attacking_up", "attacking_down", "attacking_forward"] and random.random() < 0.5:
                    self.states["blocking_" + player_state.split("_")[1]] = True
                    self.in_animation = True
                    self.states["idle"] = False
                    

                # Random attack

                elif self.attack_cooldown <= 0 and not self.in_animation:
                    self.start_random_attack()
                    self.attack_cooldown = 60

        

        return self.enemy_x, self.enemy_y



    def chase_player(self, player_x):
        # Ajusta la posición del enemigo para perseguir al jugador
        if self.enemy_x < player_x:
            self.enemy_x += 1
        else:
            self.enemy_x -= 1

    def pushed(self):
        # Ajusta la posición del enemigo cuando es empujado
        if self.distance < 0:
            self.enemy_x -= 4
        else:
            self.enemy_x += 4

        self.frame_count += 1
        if self.frame_count > 20:
            self.animation_states["pushed"] = False
            self.frame_count = 0

    def start_random_attack(self):
        # Inicia un ataque aleatorio
        random_attack = random.choice(["attacking_up", "attacking_down", "attacking_forward"])
        self.animation_states[random_attack] = True
        self.states["idle"] = False
        self.in_animation = True

    def reset_animation(self):
        # Reinicia los estados de animación
        self.animation_states.update({key: False for key in self.animation_states.keys()})
        self.states.update({key: False for key in self.states.keys()})
        self.states["idle"] = True
        self.frame_count = 0

    def get_current_state(self):
        # Devuelve el estado actual del enemigo
        for state, value in self.states.items():
            if value:
                return state

        for state, value in self.animation_states.items():
            if value:
                return state

class AiAnimationManager:
    def __init__(self, sprite_sheet:str, coords: dict, sprite_size:list, state_tree:EnemyAI):
        self.sprite_sheet = sprite_sheet
        self.SPRITE_SIZE = sprite_size
        self.coords = coords
        self.state_tree = state_tree
        
        self.frame = 0
        self.frame_count = 0
        self.COL_IGNORE = 11
        self.SEC_LIMIT = 60
        px.load(self.sprite_sheet)

    def update(self, enemy_x, enemy_y):
        self.frame_count += 1
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.distance = self.state_tree.distance

        # Priorizar las animaciones sobre los estados de comportamiento
        for action, pressed in self.state_tree.animation_states.items():
            if pressed:
                self.animate(action)
                return  # Salir después de la primera animación activa

        for action, active in self.state_tree.states.items():
            if active:
                self.animate(action)
                return  # Salir después de la primera acción activa

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

    def draw(self):
        action = self.state_tree.get_current_state()
        action_coords = self.coords.get(action)
        if not action_coords:
            return

        try:
            image_x, image_y, n_image, width, height = action_coords.get('frames', [None, None, None])[self.frame]
        except IndexError:
            self.frame = 0
            image_x, image_y, n_image, width, height = action_coords.get('frames', [None, None, None])[self.frame]

        if image_x is None or image_y is None or n_image is None:
            return

        if self.distance < 0:
            px.blt(self.enemy_x, self.enemy_y, n_image, image_x, image_y, width, height, self.COL_IGNORE)
        else:
            px.blt(self.enemy_x + width, self.enemy_y, n_image, image_x, image_y, -width, height, self.COL_IGNORE)