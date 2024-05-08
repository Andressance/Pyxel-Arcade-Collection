

class InteractionManager:
    def __init__(self, player, enemy) -> None:
        self.player = player
        self.enemy = enemy

        self.frame_count = 0

    def manageDamage(self):

        if self.player.stateTree["attacking_up"] and not self.enemy.stateTree["blocking_forward"]:
            self.enemy.health -= 10

        if self.player.stateTree["attacking_down"] and not self.enemy.stateTree["blocking_down"]:
            self.enemy.health -= 10

        if self.player.stateTree["attacking_forward"] and not self.enemy.stateTree["blocking_forward"]:
            self.enemy.health -= 10
        
        if self.enemy.stateTree["attacking_up"] and not self.player.stateTree["blocking_forward"]:
            self.player.health -= 10

        if self.enemy.stateTree["attacking_down"] and not self.player.stateTree["blocking_down"]:
            self.player.health -= 10

        if self.enemy.stateTree["attacking_forward"] and not self.player.stateTree["blocking_forward"]:
            self.player.health -= 10

    
