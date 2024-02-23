import pyxel
import random

class Snake:
    def __init__(self) -> None:
        # Initialize snake position, speed, direction, length, and tail
        self.x = random.randint(0, 155)
        self.y = random.randint(0, 115)
        self.speed = 1
        self.direction = 0
        self.length = 1
        self.tail = []

    def update(self) -> None:
        # Update snake movement
        self.move()
        


    def draw(self) -> None:
        # Draw snake and its tail
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 3, 3, 1)
        for i in range(self.length - 1):
            pyxel.rect(self.tail[i][0], self.tail[i][1], 3, 3, 1)

    def move(self) -> None:
        # Move snake based on direction
        if self.direction == 0:
            self.y -= self.speed
        elif self.direction == 1:
            self.x += self.speed
        elif self.direction == 2:
            self.y += self.speed
        elif self.direction == 3:
            self.x -= self.speed

        # Change direction based on pressed keys
        if pyxel.btnp(pyxel.KEY_UP):
            self.direction = 0
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.direction = 1
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.direction = 2
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.direction = 3

        # Move snake tail
        if self.length > 1:
            ++self.length
            self.tail.append([self.x, self.y])
            for i in range(self.length - 1, 0, -1):
                self.tail[i] = self.tail[i-1]
            self.tail[0] = [self.x, self.y]



            

    def check_tail_collision(self) -> bool:
        # Check collision with snake tail
        for i in range(self.length - 1):
            if self.x == self.tail[i][0] and self.y == self.tail[i][1] and i != 0:
                return True
        return False
