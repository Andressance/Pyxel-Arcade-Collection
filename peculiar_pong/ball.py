import pyxel as px
import random

class Ball:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.dx = random.choice([-1, 1])
        self.dy = 1
        self.clicked = False
        self.gravity = 0.07  # Adjust gravity force as needed
        self.friction = 0.985  # Adjust friction factor to simulate air resistance
        px.load("assets/resources.pyxres")

    def update(self, paddle_num, paddle_x, paddle_y, paddle_length):
        if px.btnp(px.MOUSE_BUTTON_LEFT):
            self.clicked = True
        if self.clicked:
            self.physics()
            self.paddle_collision(paddle_num, paddle_x, paddle_y, paddle_length, 4)

    def draw(self) -> None:
        self.draw_direction()

    def draw_direction(self) -> None:
        if self.dx > 0:
            if self.dy > 0:
                px.blt(self.x, self.y, 0, 22, 38, 4, 4, 0)
            elif self.dy < 0:
                px.blt(self.x, self.y, 0, 22, 22, 4, 4, 0)
        elif self.dx < 0:
            if self.dy > 0:
                px.blt(self.x, self.y, 0, 22, 54, 4, 4, 0)
            elif self.dy < 0:
                px.blt(self.x, self.y, 0, 22, 6, 4, 4, 0)

    def table_collision(self):
        if self.y + 4 > 95 and self.dy > 0:
            self.dy *= -1.1  # Increase vertical bounce factor when colliding with bottom of the table
        if self.y < 0 and self.dy < 0:
            self.dy *= -1.1  # Increase vertical bounce factor when colliding with top of the table
        if self.x < 0 and self.dx < 0:
            self.dx *= -1.1  # Increase horizontal bounce factor when colliding with left side of the table
        if self.x + 4 > 160 and self.dx > 0:
            self.dx *= -1.1  # Increase horizontal bounce factor when colliding with right side of the table

        # Prevent from going through the net
        if (self.y + 4 > 80 and self.y + 4 < 95) and (self.x + 4 > 79 and self.x < 81):
            self.dy *= -1.1
            self.dx *= -1.1

    def paddle_collision(self, paddle_num, paddle_x, paddle_y, paddle_length, collision_margin):
        if paddle_num == 1:
            paddle_x += 4
            paddle_y += 11
        else:
            paddle_x += 4
            paddle_y += 4

        # Convert paddle and ball coordinates to integers
        paddle_x = int(paddle_x)
        paddle_y = int(paddle_y)
        ball_position = (int(self.x + 2), int(self.y + 2))  # Center coordinates of the ball

        # Check if the ball is near any paddle points
        for i in range(paddle_length):
            if abs(paddle_x + i - ball_position[0]) <= collision_margin and abs(paddle_y + i - ball_position[1]) <= collision_margin or abs(paddle_x + i - ball_position[0]) <= collision_margin and abs(paddle_y - i - ball_position[1]) <= collision_margin:
                # Collision detected with the paddle
                # Calculate the bounce angle based on collision position
                angle = 1 - 2 * (ball_position[0] - paddle_x) / paddle_length
                # Adjust bounce strength
                self.dx = angle * 1.3  # Reduce the multiplicative factor to decrease bounce strength
                self.dy *= -1  # Invert the vertical direction
                return  # Exit loop once collision is detected

    def physics(self):
        # Apply gravity
        self.dy += self.gravity  # Increase vertical velocity to simulate smoother gravity

        # Apply friction
        self.dx *= self.friction
        self.dy *= self.friction

        # Update position
        self.y += self.dy
        self.x -= self.dx

        # Handle collisions
        self.table_collision()
