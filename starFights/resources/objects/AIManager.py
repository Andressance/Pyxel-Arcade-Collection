import random
import pyxel as px

class EnemyAI:
    def __init__(self, enemy_x, enemy_y, enemy_health):
        self.enemy_x, self.enemy_y = enemy_x, enemy_y
        self.enemy_health = enemy_health
        
        # Create a dictionary with all possible enemy states and initialize them as False
        self.states = {
            "idle": True,
            "chasing": False,
            "attacking_top": False,
            "attacking_bot": False,
            "attacking_mid": False,
            "force_pushing": False,
            "blocking_top": False,
            "blocking_bot": False,
            "blocking_mid": False
        }
        self.frame_count = 0

        self.before_state = "idle"
        self.distance = 0

    def update(self, player_x, player_y, player_state):
        # Update the enemy state based on player position or other conditions
        self.update_state(player_x, player_y, player_state)

        # Update the enemy based on its state
        if self.states["idle"]:
            self.idle_behavior()
        elif self.states["chasing"]:
            self.chasing_behavior(player_x)
        elif self.states["attacking_top"]:
            self.attacking_top_behavior(player_x, player_y)
        elif self.states["attacking_bot"]:
            self.attacking_bot_behavior(player_x, player_y)
        elif self.states["attacking_mid"]:
            self.attacking_mid_behavior(player_x, player_y)
        elif self.states["force_pushing"]:
            self.force_pushing_behavior(player_x, player_y)
        elif self.states["blocking_top"] or self.states["blocking_bot"] or self.states["blocking_mid"]:
            self.blocking_behavior()

        return self.enemy_x, self.enemy_y

    def update_state(self, player_x, player_y, player_state):
        # Logic to update enemy state based on player position or other conditions

        self.before_state = self.get_current_state()

        self.distance = self.enemy_x - player_x
        distance_x = abs(self.distance)
        distance_y = abs(self.enemy_y - player_y)

        if distance_x <= 50 and distance_y <= 50:
            self.states["idle"] = True
            self.states["chasing"] = False

            # If the player is attacking, there is a 33% chance that the enemy will block
            if (player_state == "attacking_up" or player_state == "attacking_down" or player_state == "attacking_forward") and random.random() <= 0.33:
                
                if player_state == "attacking_up":
                    self.states["blocking_top"] = True
                    self.states["blocking_bot"] = False
                    self.states["blocking_mid"] = False
                elif player_state == "attacking_down":
                    self.states["blocking_bot"] = True
                    self.states["blocking_top"] = False
                    self.states["blocking_mid"] = False
                elif player_state == "attacking_forward":
                    self.states["blocking_mid"] = True
                    self.states["blocking_top"] = False
                    self.states["blocking_bot"] = False

            else:

                self.states["blocking_top"] = False
                self.states["blocking_bot"] = False
                self.states["blocking_mid"] = False

        else:
            self.states["chasing"] = True
            self.states["idle"] = False
            
    def idle_behavior(self):
        pass

    def chasing_behavior(self, player_x):
        if (self.enemy_x < player_x):
            self.enemy_x += 0.75
        else:
            self.enemy_x -= 0.75


    def attacking_top_behavior(self, player_x, player_y):
        # Behavior when enemy is attacking the player from top
        pass

    def attacking_bot_behavior(self, player_x, player_y):
        # Behavior when enemy is attacking the player from bottom
        pass

    def attacking_mid_behavior(self, player_x, player_y):
        # Behavior when enemy is attacking the player from middle
        pass

    def force_pushing_behavior(self, player_x, player_y):
        # Behavior when enemy is force pushing the player
        pass

    def blocking_behavior(self):
        # Behavior when enemy is blocking
        pass

    # Other methods for other behaviors and actions of the enemy

    def get_current_state(self):
        # Return the current state of the enemy
        for state, value in self.states.items():
            if value:
                return state

class AiAnimationManager:
    def __init__(self, sprite_sheet:str,  idle_coords:list, walk_coords:list, mid_attack_coords:list, 
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
        elif self.stateTree.states["attacking_top"]:
            self.top_attack_animation()
        elif self.stateTree.states["attacking_bot"]:
            self.bot_attack_animation()
        elif self.stateTree.states["attacking_mid"]:
            self.mid_attack_animation()
        elif self.stateTree.states["force_pushing"]:
            self.force_pushing_animation()
        elif self.stateTree.states["blocking_top"] or self.stateTree.states["blocking_bot"] or self.stateTree.states["blocking_mid"]:
            self.block_animation()

    def idle_animation(self):
        self.frame_count += 1
        
        if self.stateTree.before_state != "idle":
            self.frame = 0
            self.frame_count = 0

        if self.frame_count > 10:
            self.frame += 1
            if self.frame > 0:
                self.frame = 0
            self.frame_count = 0

    def walk_animation(self):
        self.frame_count += 1

        if self.stateTree.before_state != "chasing":
            self.frame = 0
            self.frame_count = 0

        if self.frame_count > 15:
            self.frame += 1
            if self.frame > 5:
                self.frame = 0
            self.frame_count = 0
            

    def draw(self, characterX, characterY, distance):
        if self.stateTree.states["idle"]:
            image_x, image_y, n_image, width, height = self.idle_coords[self.frame]
            px.blt(characterX, characterY, n_image, image_x, image_y, width, height, self.COL_IGNORE)

        elif self.stateTree.states["chasing"]:
            image_x, image_y, n_image, width, height = self.walk_coords[self.frame]
            
            if distance < 0:
                px.blt(characterX, characterY, n_image, image_x, image_y, width, height, self.COL_IGNORE)
            else:
                px.blt(characterX, characterY, n_image, image_x, image_y, -width, height, self.COL_IGNORE)


            
