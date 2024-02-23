import pyxel
import snake
import hud
import apple

class App:
    def __init__(self):
        # Initialize Pyxel window
        pyxel.init(160, 120)
        # Initialize player, game start and game over states, and apple
        self.player = snake.Snake()
        self.game_start = False
        self.game_over = False
        self.apple = apple.Apple()
        # Run game loop
        pyxel.run(self.update, self.draw)
        

    def update(self) -> None:
        # Handle game over and restart
        if self.game_over and pyxel.btnp(pyxel.KEY_SPACE):
            self.restart()

        # Handle game start
        if not self.game_start:
            if pyxel.btnp(pyxel.KEY_UP):
                self.player.direction = 0
                self.game_start = True
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.player.direction = 1
                self.game_start = True
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.player.direction = 2
                self.game_start = True
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.player.direction = 3
                self.game_start = True
        # Update game state if game is not over
        if not self.game_over:
            if self.game_start: 
                self.player.update()
                self.collision_apple() 
                self.check_collision()
                if self.player.check_tail_collision():
                   self.game_over = True                   

        


        

    def draw(self) -> None:
        # Draw player, HUD, apple, and game over message
        self.player.draw()
        if not self.game_start:
            hud.press_to_start() 
        hud.show_score(self.player.length - 1 )
        self.apple.draw()
        if self.game_over:
            hud.game_over()

    def check_collision(self) -> None:
        # Check collision with screen boundaries
        if self.player.x > 160 or self.player.x < 0 or self.player.y > 120 or self.player.y < 0:
            self.game_over = True
            

    def collision_apple(self):
        # Check collision with apple and update player length and speed
        if self.player.x in range(self.apple.x -3 , self.apple.x + 3) and self.player.y in range(self.apple.y - 3, self.apple.y + 3):
            self.apple = apple.Apple()
            self.player.length += 1
            self.player.tail.append([self.player.x, self.player.y])

        if self.player.length - 1 % 10 == 0 and self.player.length > 1:
            self.player.speed += 0.05
    
    def restart(self):
        # Restart game
        self.player = snake.Snake()
        self.game_start = False
        self.game_over = False
        self.apple = apple.Apple()

       
if __name__ == "__main__":
    App()
