import pyxel as px 

class Player:
    def __init__(self, x, y, num_player) -> None:
        """
        Initialize the player with its position and controls.

        Args:
            x (int): The initial x-coordinate of the player.
            y (int): The initial y-coordinate of the player.
            num_player (int): The player number (1 or 2).
        """
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.num = num_player
        # Define the control keys based on the player number
        self.keys = [px.KEY_W, px.KEY_S, px.KEY_A, px.KEY_D] if self.num == 1 else [px.KEY_UP, px.KEY_DOWN, px.KEY_LEFT, px.KEY_RIGHT]
        self.MAX_Y = 100
        self.MIN_Y = 50
        self.MAX_X = 100 if self.num == 1 else 50
        self.MIN_X = 50 if self.num == 1 else 0
        px.load("assets/resources.pyxres")  # Load player sprites

    def update(self) -> None:
        """
        Update the player's position based on the pressed keys.
        """
        # Move the player up if the W or UP key is pressed
        if px.btn(self.keys[0]):
            if self.y > self.MIN_Y:
                self.y -= 1.25
        # Move the player down if the S or DOWN key is pressed
        if px.btn(self.keys[1]):
            if self.y < self.MAX_Y:
                self.y += 1.25
        # Move the player left if the A or LEFT key is pressed
        if px.btn(self.keys[2]):
            self.x -= 1.25
        # Move the player right if the D or RIGHT key is pressed
        if px.btn(self.keys[3]):
            self.x += 1.25

    def draw(self) -> None:
        """
        Draw the player sprite on the screen.
        """
        # Draw the player sprite based on its number
        if self.num == 1:
            px.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)  # Draw player 1 sprite
        else:
            px.blt(self.x, self.y, 0, 0, 16, 16, 16, 0)  # Draw player 2 sprite
