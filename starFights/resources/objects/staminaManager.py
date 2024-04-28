from random import randint

class StaminaManager:
    def __init__(self, stamina:int ,maxStamina:int, stateTree):
    
        self.stamina = stamina
        self.MAX_STAMINA = maxStamina

        self.frame_count = 0
        self.stateTree = stateTree

    def update(self, stamina:int, stateTree):
        self.stamina = stamina
        self.stateTree = stateTree
        self.manage_stamina()
        return self.stamina
        
    def manage_stamina(self):

        self.frame_count += 1

        if self.stateTree.is_attacking():
            if self.frame_count > 30:
                if self.stamina >= 15:
                    self.stamina -= 15
                    self.frame_count = 0

        # If the player does not attack in 60 frames, regenerate stamina
        if self.frame_count > randint(40, 60):
            self.stamina += 5
            self.frame_count = 0

        # if the player has no stamina, he can't attack
        if self.stamina < 0:
            self.stateTree.states["attacking_up"] = False
            self.stateTree.states["attacking_down"] = False
            self.stateTree.states["attacking_forward"] = False
            self.stamina = 0
            self.frame_count = 0

        # If the player has more than 100 stamina, set it to 100
        if self.stamina > 100:
            self.stamina = 100