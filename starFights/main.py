import pyxel as px
from resources.hud.hud import Hud
from resources.objects.player import Player
from resources.objects.enemy import Enemy

class Game:
    def __init__(self):
        self.x_size, self.y_size = 500, 328
        px.init(self.x_size, self.y_size, "Star Fights", 60)
        self.player = None
        self.enemy = None
        self.hud = Hud(self.x_size, self.y_size)
        px.run(self.update, self.draw)
        

    def update(self):
    
        if not self.hud.in_game:
            self.hud.update()
        else:
            if self.player is None: # We create the player only if its not created # We create the player only if its not created
                self.player = Player(50, 200, 100)
            if self.enemy == None:
                self.enemy = Enemy(350, 200, 100)
            self.player.update()
            self.enemy.update(self.player.x, self.player.y, self.player.stateTree.before_state)
            

    def draw(self):
        px.cls(0)
        if not self.hud.in_game:
            self.hud.draw()
        else:
            if self.player is not None:
                px.load("resources/sprites/sprites.pyxres")
                self.player.draw()
            if self.enemy is not None:
                px.load("resources/sprites/enemy.pyxres")
                self.enemy.draw()

if __name__ == "__main__":
    Game()