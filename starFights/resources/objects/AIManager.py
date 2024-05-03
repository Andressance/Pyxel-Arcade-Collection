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
        }
        self.in_animation = False

        self.before_state = "idle"
        self.distance = 0
        self.attack_cooldown = 0

        self.frame_count = 0

    def update(self, player_x, player_y, player_state):
        self.enemy_x, self.enemy_y = self.update_states(player_x, player_y, player_state)

        if self.states["chasing"]:
            self.chase_player()

        return self.enemy_x, self.enemy_y

    def update_states(self, player_x, player_y, player_state):
        self.before_state = self.get_current_state()
        self.distance = self.enemy_x - player_x
        if self.in_animation:
            self.frame_count += 1
            if self.frame_count > 30:
                self.in_animation = False
                self.frame_count = 0
                self.attack_cooldown = random.randint(60, 100)
        else:
            # Si el enemigo está dentro del rango de ataque del jugador
            if abs(self.enemy_x - player_x) <= 50:
                self.states["chasing"] = False
                # Probabilidad de éxito en el bloqueo
                success_block = random.random() <= 0.55
                # Determinar si el jugador está atacando y bloquear si es necesario
                if player_state == "attacking_up" and (success_block or self.in_animation):
                    self.states["blocking_up"] = True
                    self.in_animation = True
                elif player_state == "attacking_down" and (success_block or self.in_animation):
                    self.states["blocking_down"] = True
                    self.in_animation = True
                elif player_state == "attacking_forward" and (success_block or self.in_animation):
                    self.states["blocking_forward"] = True
                    self.in_animation = True
                else:
                    # Si el jugador no está atacando ni bloqueando, el enemigo entra en estado "idle"
                    self.states["idle"] = True
                    self.states["blocking_up"] = False
                    self.states["blocking_down"] = False
                    self.states["blocking_forward"] = False
                    self.attack_cooldown = max(0, self.attack_cooldown - 1)
                    if random.randint(0, 1) == 1 and self.attack_cooldown == 0:
                        random_attack = random.choice(["attacking_up", "attacking_down", "attacking_forward"])
                        self.animation_states[random_attack] = True
                        self.states["idle"] = False
                        self.in_animation = True
            else:
                # Si el enemigo está fuera del rango de ataque, persigue al jugador
                self.states["chasing"] = True
                self.states["idle"] = False
        
        # Restablecer estados de bloqueo después de un bloqueo exitoso y permitir que el enemigo ataque antes de bloquear nuevamente
        if self.before_state in ["blocking_up", "blocking_down", "blocking_forward"] and not self.in_animation:
            self.states["blocking_up"] = False
            self.states["blocking_down"] = False
            self.states["blocking_forward"] = False
    

        print(self.get_current_state())
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            
        return self.enemy_x, self.enemy_y




        

    def chase_player(self):

        if self.distance < 0:
            self.enemy_x += 1
        else:
            self.enemy_x -= 1


    def get_current_state(self):
        for state, value in self.states.items():
            if value:
                return state
            
        for state, value in self.animation_states.items():
            if value:
                return state

class AiAnimationManager:
    def __init__(self, sprite_sheet:str, idle_coords:list, walk_coords:list, mid_attack_coords:list, 
                bot_attack_coords:list, top_attack_coords:list, force_pushing_coords:list, block_coords:list, stateTree:EnemyAI):
        self.sprite_sheet = sprite_sheet
        self.idle_coords = idle_coords
        self.walk_coords = walk_coords
        self.mid_attack_coords = mid_attack_coords
        self.bot_attack_coords = bot_attack_coords
        self.top_attack_coords = top_attack_coords
        self.force_pushing_coords = force_pushing_coords
        self.block_coords = block_coords
        self.stateTree = stateTree
        self.frame = 0
        self.COL_IGNORE = 11
        self.frame_count = 0

    def update(self, enemy_x, enemy_y):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.frame_count += 1

        if self.stateTree.states["idle"]:
            self.idle_animation()
        elif self.stateTree.states["chasing"]:
            self.walk_animation()
        elif self.stateTree.states["attacking_up"] or self.stateTree.states["attacking_down"] or self.stateTree.states["attacking_forward"]:
            self.attack_animation()
        elif self.stateTree.states["blocking_up"] or self.stateTree.states["blocking_down"] or self.stateTree.states["blocking_forward"]:
            self.block_animation()

    def idle_animation(self):
        self.frame_count += 1
        if self.stateTree.before_state != "idle":
            self.frame = 0
            self.frame_count = 0
        if self.frame_count > 120:
            self.frame += 1
            if self.frame > len(self.idle_coords) - 1:
                self.frame = 0
            self.frame_count = 0

    def walk_animation(self):
        self.frame_count += 1
        if self.stateTree.before_state != "chasing":
            self.frame = 0
            self.frame_count = 0
        if self.frame_count > 15:
            self.frame += 1
            if self.frame > len(self.walk_coords) - 1:
                self.frame = 0
            self.frame_count = 0

    def attack_animation(self):
        self.frame_count += 1
        if self.frame_count > len(self.mid_attack - 1):
            self.frame_count = 0

class AiAnimationManager:
    def __init__(self, sprite_sheet:str, idle_coords:list, walk_coords:list, mid_attack_coords:list, 
                bot_attack_coords:list, top_attack_coords:list, force_pushing_coords:list, block_coords:list, stateTree:EnemyAI):
        self.sprite_sheet = sprite_sheet
        self.idle_coords = idle_coords
        self.walk_coords = walk_coords
        self.mid_attack_coords = mid_attack_coords
        self.bot_attack_coords = bot_attack_coords
        self.top_attack_coords = top_attack_coords
        self.force_pushing_coords = force_pushing_coords
        self.block_coords = block_coords

        self.stateTree = stateTree
        self.frame = 0
        self.COL_IGNORE = 11
        self.frame_count = 0

    def update(self, enemy_x, enemy_y):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.frame_count += 1

        if self.stateTree.states["idle"]:
            self.idle_animation()
        elif self.stateTree.states["chasing"]:
            self.walk_animation()
        elif self.stateTree.animation_states["attacking_up"] or self.stateTree.animation_states["attacking_down"] or self.stateTree.animation_states["attacking_forward"]:
            self.attack_animation()
        elif self.stateTree.states["blocking_up"] or self.stateTree.states["blocking_down"] or self.stateTree.states["blocking_forward"]:
            self.block_animation()

    def idle_animation(self):
        self.frame_count += 1
        if self.stateTree.before_state != "idle":
            self.frame = 0
            self.frame_count = 0
        if self.frame_count > 120:
            self.frame += 1
            if self.frame > len(self.idle_coords) - 1:
                self.frame = 0
            self.frame_count = 0

    def walk_animation(self):
        self.frame_count += 1
        if self.stateTree.before_state != "chasing":
            self.frame = 0
            self.frame_count = 0
        if self.frame_count > 15:
            self.frame += 1
            if self.frame > len(self.walk_coords) - 1:
                self.frame = 0
            self.frame_count = 0

    def attack_animation(self):
        pass
        #self.frame_count += 1
        #if self.frame_count > len(self.attack_coords) - 1:
        #    self.frame_count = 0

    def block_animation(self):
        pass

    def draw(self, characterX, characterY, distance):
        if self.stateTree.states["idle"]:
            image_x, image_y, n_image, width, height = self.idle_coords[self.frame]
            if distance < 0:
                px.blt(characterX, characterY, n_image, image_x, image_y, width, height, self.COL_IGNORE)
            else:
                px.blt(characterX, characterY, n_image, image_x, image_y, -width, height, self.COL_IGNORE)
        elif self.stateTree.states["chasing"]:
            image_x, image_y, n_image, width, height = self.walk_coords[self.frame]
            if distance < 0:
                px.blt(characterX, characterY, n_image, image_x, image_y, width, height, self.COL_IGNORE)
            else:
                px.blt(characterX, characterY, n_image, image_x, image_y, -width, height, self.COL_IGNORE)
