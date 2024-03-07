import pyxel as px
import threading
import random
from time import sleep

class Bus:
    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y
        self.speed = 1
        self.sprite = 0
        self.width = 16
        self.height = 39

    def update(self):
        self.y += self.speed

    def draw(self):
        px.blt(self.x, self.y, 0, 0, 74, self.width, self.height, 3)
