import pyxel
from random import randint

class Ball:
    def __init__(self) -> None:
        # Initialize ball position and speed
        self.x = 80
        self.y = 60
        self.speedX = -1.0 if randint(0, 1) == 0 else 1.0
        self.speedY = -1.5 if randint(0, 1) == 0 else 1.5
        self.r = 2
        self.out_of_bounds = False

    def draw(self):
        # Draw ball
        pyxel.circ(self.x, self.y, self.r, 7)

    def update(self):
        # Update ball position
        self.x += self.speedX
        self.y += self.speedY
        
        # Reflect ball if it hits top or bottom boundaries
        if self.y < 0 or self.y > 120:
            self.speedY *= -1
        
    
    def reset(self):
        # Reset ball position and speed
        self.x = 80
        self.y = 60
        self.speedX = -1.0 if randint(0, 1) == 0 else 1.0
        self.speedY = -1.5 if randint(0, 1) == 0 else 1.5
        self.out_of_bounds = False
