import pyxel as px  
import threading  # Import threading library for concurrent operations
import random  # Import random library for generating random numbers
from time import sleep  # Import sleep function from time module

class Bike:
    def __init__(self, x, y) -> None:
        self.x = x  # X-coordinate of the bike
        self.y = y  # Y-coordinate of the bike
        self.speed = 1  # Speed of the bike
        self.sprite = 0  # Sprite index of the bike
        self.width = 16  # Width of the bike sprite
        self.height = 27  # Height of the bike sprite

    def update(self):
        self.y += self.speed  # Update the y-coordinate based on the speed

    def draw(self):
        px.blt(self.x, self.y, 0, 48, 72, self.width, self.height, 3)  # Draw the bike sprite
