import pyxel
import random

class Apple:
    def __init__(self) -> None:
        # Initialize apple position randomly
        self.x = random.randint(0, 155)
        self.y = random.randint(0, 115)

    def draw(self) -> None:
        # Draw apple
        pyxel.rect(self.x, self.y, 3, 3, 8)
