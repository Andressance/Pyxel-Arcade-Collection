import pyxel as px
from time import sleep
import threading

class Car:
    def __init__(self) -> None:
        self.position = 1
        self.target_position = self.position
        self.animation_timer = 0
        self.animation_duration = 0.6
        self.direction = 0
        self.speed = 0.01
        self.x = 50
        self.y = 100
        self.smoke = 0

    def update(self) -> None:
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

        self.target_position = max(0, min(self.target_position, 2))

        self.position += self.direction * self.speed

        if round(self.position, 1) == self.target_position:
            self.animation_timer = 0

        if self.position != self.target_position:
            self.animation_timer += 0.01
            if self.animation_timer >= self.animation_duration:
                self.animation_timer = 0
                self.position = self.target_position
            else:
                progress = self.animation_timer / self.animation_duration
                self.position = self.target_position * progress + self.position * (1 - progress)
                
        if self.position == 1:
            self.x = 50
        else:
            self.x = 15 + self.position * 35

    def smooth_interpolate(self, t):
        return t * t * (3 - 2 * t)

    def draw(self) -> None:
        self.draw_car()
        threading.Thread(target=self.draw_smoke).start()

    def draw_car(self) -> None:
        px.blt(self.x, self.y, 0, 0, 16, 16, 24, 3)

    def draw_smoke(self) -> None:
        car_width = 16
        car_height = 24

        car_back_y = self.y + car_height - 4
        smoke_x = (self.x + car_width / 2) + 2

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

        sleep(0.2)
