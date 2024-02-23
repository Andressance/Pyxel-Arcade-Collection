import pyxel

class Player():
    def __init__(self, keyUp, keyDown, x) -> None:
        # Initialize player position, dimensions, and controls
        self.x = x
        self.y = 50
        self.w = 3
        self.h = 20
        self.keyUp = keyUp
        self.keyDown = keyDown
        self.speed = 0

    def draw(self):
        # Draw player
        pyxel.rect(self.x, self.y, self.w, self.h, 7)

    def update(self):
        # Update player position based on pressed keys
        if pyxel.btn(self.keyUp):
            self.y -= 1.5
        if pyxel.btn(self.keyDown):
            self.y += 1.5

        # Keep player within screen boundaries
        if self.y < 0:
            self.y = 0
        if self.y > 120 - self.h:
            self.y = 120 - self.h

    def reset(self): 
        # Reset player position
        self.y = 50
