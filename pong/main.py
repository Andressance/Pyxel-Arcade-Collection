import pyxel
import ball
import player
import hud

class App():
    def __init__(self) -> None:
        pyxel.init(160, 120,"Pong", fps=60)
        self.ball = ball.Ball()
        self.player1 = player.Player(pyxel.KEY_W, pyxel.KEY_S, 0)
        self.player2 = player.Player(pyxel.KEY_UP, pyxel.KEY_DOWN, 157)
        self.score = [0, 0]
        self.game_over = False
        self.pause = True
        pyxel.run(self.update, self.draw)

    def update(self):
        # Toggle pause state when SPACE is pressed
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.pause = not self.pause

        if not self.pause:
            # Update player positions
            self.player1.update()
            self.player2.update()
            # Check for out-of-bounds and winners
            self.check_out_of_bounds()
            self.check_winner()
            if self.game_over:
                # Reset game on SPACE press after game over
                if pyxel.btnp(pyxel.KEY_SPACE):
                    self.reset_game()
            # Update ball position
            self.ball.update()
            # Display score
            hud.show_score(self.score[0], self.score[1])
        else:
            # Display "Press SPACE to play" when paused
            hud.press_to_play()

    def draw(self):
        # Clear screen
        pyxel.cls(0)
        # Draw ball and players
        self.ball.draw()
        self.player1.draw()
        self.player2.draw()
        # Detect collisions between ball and players
        self.detect_collision()
        # Display score
        pyxel.text(50, 0, f"Score: {self.score}", 7)
        # Display game over message and "Press SPACE to play" when game over
        if self.game_over:
            if self.score[0] == 5:
                pyxel.text(55, 55, "Player 1 Wins", 8)
            else:
                pyxel.text(45, 40, "Player 2 Wins", 8)
            hud.game_over()

        # Display "Press SPACE to play" when paused and game not over
        if self.pause and not self.game_over:
            hud.press_to_play()

    def detect_collision(self):
        # Detect collision between ball and player 1
        if self.ball.x > self.player1.x and self.ball.x < self.player1.x + self.player1.w:
            if self.ball.y > self.player1.y and self.ball.y < self.player1.y + self.player1.h:
                self.ball.speedX *= -1.2

        # Detect collision between ball and player 2
        if self.ball.x > self.player2.x and self.ball.x < self.player2.x + self.player2.w:
            if self.ball.y > self.player2.y and self.ball.y < self.player2.y + self.player2.h:
                self.ball.speedX *= -1.2

    def check_out_of_bounds(self):
        # Check if ball goes out of bounds and update score accordingly
        if self.ball.x < 0:
            self.ball.out_of_bounds = True
            self.ball.reset()
            self.player1.reset()
            self.player2.reset()
            self.score[1] += 1
            self.pause = True
        if self.ball.x > 160:
            self.ball.out_of_bounds = True
            self.ball.reset()
            self.player1.reset()
            self.player2.reset()
            self.score[0] += 1
            self.pause = True
        return self.ball.out_of_bounds

    def check_winner(self):
        # Check for winner and set game_over state
        if self.score[0] == 5 or self.score[1] == 5:
            self.game_over = True
            self.pause = True
            return True
        return False
    
    def reset_game(self):
        # Reset game state
        self.score = [0, 0]
        self.game_over = False
        self.pause = True
        self.ball.reset()
        self.player1.reset()
        self.player2.reset()
 
                
if __name__ == "__main__":
    App()
