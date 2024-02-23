import pyxel as px
import hud
import random
from table import Table
from ball import Ball
from player import Player
from goal import Goal

def main():
    # Initialize Pyxel window
    px.init(160, 120, "Ping Pong")

    # Create game objects
    table = Table(40, 80)
    player2 = Player(107.5, 80, 1)
    player = Player(36.25, 80, 2)
    ball = Ball(80, 60)
    goal = Goal(30, 50)
    goal2 = Goal(130, 50)
    score = [0, 0]
    click = False

    def update() -> None:
        nonlocal click

        # Restart game if 'R' key is pressed
        if px.btnp(px.KEY_R):
            reset_play()

        # Detect mouse click to start the game
        if px.btnp(px.MOUSE_BUTTON_LEFT):
            px.text(60, 20, "Click to start", 7)
            click = True

        # If game is not started yet, keep the ball stationary
        if not click:
            ball.x = ball.x
            ball.y = ball.y
        else:
            # Update ball position and players' movement
            ball.update(player.num, player.x, player.y, 8)
            ball.update(player2.num, player2.x, player2.y, 8)
            player.update()
            player2.update()

            # Check for goals and bugs in ball movement
            check_goal()
            check_ball_bug()

    def draw() -> None:
        px.cls(0)
        # Draw game elements
        ball.draw()
        table.draw()
        player.draw()
        player2.draw()
        goal.draw()
        goal2.draw()
        hud.show_score(score[0], score[1])

    def check_goal() -> None:
        nonlocal score

        # Check if the ball enters either goal area
        if ball.x < goal.x and ball.y > goal.y and ball.y < goal.y + 40:
            score[1] += 1
            reset_play()
        if ball.x > goal2.x and ball.y > goal2.y and ball.y < goal2.y + 40:
            score[0] += 1
            reset_play()

    def reset_play():
        # Reset game state and ball position
        global click
        click = False
        ball.x = 80
        ball.y = 60
        ball.dx = random.choice([-1, 1])

    def check_ball_bug():
        # Reset game if ball goes out of bounds or has no vertical movement
        if ball.x < 0 or ball.x > 160 or ball.y < 0 or ball.y > 120:
            reset_play()
        if ball.dy == 0:
            reset_play()

    # Run game loop
    px.run(update, draw)

if __name__ == "__main__":
    main()
