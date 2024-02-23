import pyxel as px

class Goal:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def update(self) -> None:
        pass

    def draw(self) -> None:
        px.rect(self.x, self.y, 3, 40, 8)
