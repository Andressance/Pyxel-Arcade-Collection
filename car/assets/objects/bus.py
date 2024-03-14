import pyxel as px  
import threading  # Import threading library for concurrent operations
import random  # Import random library for generating random numbers
from time import sleep  # Import sleep function from time module

class Bus:
    def __init__(self, x, y) -> None:
        self.x = x  # X-coordinate of the bus
        self.y = y  # Y-coordinate of the bus
        self.speed = 1  # Speed of the bus
        self.sprite = 0  # Sprite index of the bus
        self.width = 16  # Width of the bus sprite
        self.height = 39  # Height of the bus sprite

    def update(self):
        self.y += self.speed  # Update the y-coordinate based on the speed

    def draw(self):
        px.blt(self.x, self.y, 0, 0, 74, self.width, self.height, 3)  # Draw the bus sprite
