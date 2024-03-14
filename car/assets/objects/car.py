import pyxel as px  # Import Pyxel library for game development
from time import sleep  # Import sleep function from time module
import threading  # Import threading library for concurrent operations

class Car:
    def __init__(self) -> None:
        self.position = 1  # Current position of the car (0: left, 1: center, 2: right)
        self.target_position = self.position  # Target position to move towards
        self.animation_timer = 0  # Timer for animation
        self.animation_duration = 0.6  # Duration of the animation
        self.direction = 0  # Direction of movement (-1: left, 1: right)
        self.speed = 0.01  # Speed of movement
        self.x = 50  # Initial x-coordinate of the car
        self.y = 100  # Initial y-coordinate of the car
        self.smoke = 0  # Counter for smoke animation

    def update(self) -> None:
        # Check for keyboard input to move the car left or right
        if px.btn(px.KEY_RIGHT):
            if self.position < 2:
                self.target_position = self.position + 1
                self.direction = 0.3
                self.speed = 0.005
        elif px.btn(px.KEY_LEFT):
            if self.position > 0:
                self.target_position = self.position - 1
                self.direction = -0.3
                self.speed = 0.005
        else:
            self.direction = 0

        # Ensure the target position is within bounds
        self.target_position = max(0, min(self.target_position, 2))

        # Update the position based on direction and speed
        self.position += self.direction * self.speed

        # Check if the animation is complete
        if round(self.position, 1) == self.target_position:
            self.animation_timer = 0

        # Perform smooth animation towards the target position
        if self.position != self.target_position:
            self.animation_timer += 0.01
            if self.animation_timer >= self.animation_duration:
                self.animation_timer = 0
                self.position = self.target_position
            else:
                progress = self.animation_timer / self.animation_duration
                self.position = self.target_position * progress + self.position * (1 - progress)
                
        # Update the x-coordinate of the car based on its position
        if self.position == 1:
            self.x = 50
        else:
            self.x = 15 + self.position * 35

    def draw(self) -> None:
        self.draw_car()  # Draw the car
        threading.Thread(target=self.draw_smoke).start()  # Start a thread to draw smoke

    def draw_car(self) -> None:
        px.blt(self.x, self.y, 0, 0, 16, 16, 24, 3)  # Draw the car sprite

    def draw_smoke(self) -> None:
        car_width = 16  # Width of the car sprite
        car_height = 24  # Height of the car sprite

        car_back_y = self.y + car_height - 4  # Y-coordinate of the back of the car
        smoke_x = (self.x + car_width / 2) + 2  # X-coordinate for drawing smoke

        # Draw smoke animation based on the smoke counter
        if self.smoke == 0:
            px.blt(smoke_x, car_back_y, 0, 19, 31, 8, 5, 3)
            self.smoke += 1
        elif self.smoke == 1:
            px.blt(smoke_x, car_back_y, 0, 34, 32, 8, 5, 3)
            self.smoke += 1
        elif self.smoke == 2:
            px.blt(smoke_x, car_back_y, 0, 50, 27, 8, 6, 3)
            self.smoke += 1
        else:
            self.smoke = 0

        sleep(0.2)  # Pause for a short duration to control animation speed
