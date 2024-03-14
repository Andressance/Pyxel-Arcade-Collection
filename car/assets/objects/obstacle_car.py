import pyxel as px  
import threading  # Import threading library for concurrent operations
import random  # Import random library for generating random numbers
from time import sleep  # Import sleep function from time module

class ObstacleCar:
    def __init__(self, x, y) -> None:
        self.x = x  # X-coordinate of the obstacle car
        self.y = y  # Y-coordinate of the obstacle car
        self.speed = 1  # Speed of the obstacle car
        self.sprite = 0  # Sprite index of the obstacle car
        self.width = 16  # Width of the obstacle car sprite
        self.height = 32  # Height of the obstacle car sprite

    def update(self):
        self.y += self.speed  # Update the y-coordinate based on the speed

    def draw(self):
        px.blt(self.x, self.y, 0, 24, 72, self.width, self.height, 3)  # Draw the obstacle car sprite
