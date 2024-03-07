import pyxel as px
import random
from assets.objects.car import Car
from assets.objects.bus import Bus
import assets.hud as hud
from time import sleep
import threading


class App:
    def __init__(self) -> None:
        px.init(128, 130, "Car Game")
        px.load("sprites/resources.pyxres")
        self.car = Car()
        self.player_speed = 1  # Velocidad del jugador
        self.player_position = 0  # Posición inicial del jugador
        self.score = 0
        self.game_over = False
        self.obstacle_threshold = 50  # Distancia mínima entre obstáculos
        self.next_obstacle_position = self.obstacle_threshold
        self.count = 0
        self.obstacles = []
        threading.Thread(target=self.update_score).start()
        px.run(self.update, self.draw)

    def update(self) -> None:
        self.car.update()
        self.update_obstacles()
        if self.score == 50:
            for i in self.obstacles:
                i.speed += 0.2


    def draw(self) -> None:
        px.cls(3)
        self.draw_background()
        self.draw_obstacles()
        hud.show_score(self.score)
        self.car.draw()

    def update_score(self) -> None:
        while not self.game_over:
            self.score += 1
            sleep(0.5)

    def draw_background(self) -> None:
        px.bltm(0, self.count - 112, 0, 0, 0, 128, 120)
        px.bltm(0, self.count + 8, 0, 0, 0, 128, 120)
        px.rect(0, 2, 128, 15, 0)
        px.rect(0, 0, 128, 15, 7)
        sleep(0.025)
        if self.count == 120:
            self.count = 0
        
        self.count += 1

    def update_obstacles(self) -> None:
        self.player_position += self.player_speed  # Avance del jugador
        if self.player_position >= self.next_obstacle_position:
            self.create_obstacle()
            self.next_obstacle_position += self.obstacle_threshold

        for obstacle in self.obstacles:
            obstacle.update()

    def draw_obstacles(self) -> None:
        for obstacle in self.obstacles:
            obstacle.draw()

    def create_obstacle(self) -> None:
        ran = random.randint(0, 2)
        if ran == 0:
            bus = Bus(20, -20)
        elif ran == 1:
            bus = Bus(50, -20)
        else:
            bus = Bus(95, -20)

        self.obstacles.append(bus)

App()
