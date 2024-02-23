import pyxel as px

class Table:
    def __init__(self, x ,y) -> None:
        self.x = x
        self.y = y
        px.load("assets/resources.pyxres")

    def update(self) -> None:
        pass

    def draw(self) -> None:
        px.blt(self.x, self.y, 0, 32, 0, 80, 32, 0)

    
