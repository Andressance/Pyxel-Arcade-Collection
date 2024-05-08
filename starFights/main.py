import pyxel as px
from resources.hud.hud import Hud
from resources.objects.player import Player
from resources.objects.enemy import Enemy
from resources.objects.interactionsManager import InteractionManager

class Game:
    def __init__(self):
        self.x_size, self.y_size = 500, 328
        px.init(self.x_size, self.y_size, "Star Fights", 60)
        self.player = None
        self.enemy = None
        self.interactionManager = None
        px.run(self.update, self.draw)
        

    def update(self):
        if not self.hud.in_game:
            self.hud.update()
        else:
            if self.player is None:
                self.player = Player(50, 200, 100)
            if self.enemy is None:
                self.enemy = Enemy(350, 200, 100)
            if self.interactionsManager is None:
                self.interactionsManager = InteractionManager(self.player, self.enemy)
                
            self.player.update(self.enemy.x, self.enemy.y)
            self.enemy.update(self.player.x, self.player.y, self.player.stateTree.before_state)
            
            if self.player.health <= 0:
                self.hud.in_game = False
                self.player = None
                self.enemy = None


    def draw(self):
        px.cls(0)
        if not self.hud.in_game:
            self.hud.draw()
        else:
            if self.player:
                px.load("resources/sprites/sprites.pyxres")
                self.player.draw()
            if self.enemy:
                px.load("resources/sprites/enemy.pyxres")
                self.enemy.draw()

if __name__ == "__main__":
    Game()
