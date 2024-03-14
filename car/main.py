import pyxel as px  # Import Pyxel library
import random  # Import random library for generating random numbers
from assets.objects.car import Car  # Import Car class from car module
from assets.objects.bus import Bus  # Import Bus class from bus module
from assets.objects.obstacle_car import ObstacleCar  # Import ObstacleCar class from obstacle_car module
from assets.objects.bike import Bike  # Import Bike class from bike module
import assets.hud as hud  # Import hud module for heads-up display
from time import sleep  # Import sleep function from time module
import threading  # Import threading library for concurrent operations

class App:
    def __init__(self) -> None:
        px.init(128, 130, "Car Game")  # Initialize Pyxel with screen size and game title
        px.load("sprites/resources.pyxres")  # Load graphic resources
        self.car = Car()  # Create an instance of the player's car
        self.player_speed = 1  # Player's speed
        self.player_position = 0  # Initial player position
        self.score = 0  # Player's score
        self.game_over = False  # Flag indicating whether the game is over
        self.obstacle_threshold = 50  # Minimum distance between obstacles
        self.next_obstacle_position = self.obstacle_threshold  # Position of the next obstacle
        self.count = 0  # Counter for background animation
        self.obstacles = []  # List to store obstacles
        threading.Thread(target=self.update_score).start()  # Start a thread to update score in the background
        px.run(self.update, self.draw)  # Run the main Pyxel loop with update and draw functions

    def update(self) -> None:
        if not self.game_over:
            self.update_obstacles()  # Update obstacles
            self.car.update()  # Update player's car
            self.game_over = self.check_collision()  # Check for collisions
            if self.score == 50:
                for i in self.obstacles:
                    i.speed += 0.2
        else:
            if px.btnp(px.KEY_R):  # Restart the game if 'R' key is pressed
                self.restart()

    def draw(self) -> None:
        if not self.game_over:    
            px.cls(3)  # Clear the screen with a specific color
            self.draw_background()  # Draw the animated background
            self.car.draw()  # Draw the player's car
            self.draw_obstacles()  # Draw obstacles
            hud.display_hud()  # Show the user interface
            hud.show_score(self.score)  # Show player's score
            
        else:
            self.game_over_hud()  # Show the game over message

    def update_score(self) -> None:
        while not self.game_over:
            self.score += 1  # Increment the score
            sleep(0.5)  # Wait for half a second before updating score again

    def draw_background(self) -> None:
        px.bltm(0, self.count - 112, 0, 0, 0, 128, 120)  # Draw the animated background
        px.bltm(0, self.count + 8, 0, 0, 0, 128, 120)  # Draw the animated background
        sleep(0.025)  # Small pause for animation
        if self.count == 120:
            self.count = 0
        self.count += 1  # Increment the counter for animation

    def update_obstacles(self) -> None:
        self.player_position += self.player_speed  # Update player's position
        if self.player_position >= self.next_obstacle_position:
            self.create_obstacle()  # Create a new obstacle
            self.next_obstacle_position += self.obstacle_threshold  # Update position of the next obstacle
        for obstacle in self.obstacles:
            obstacle.update()  # Update each obstacle

    def draw_obstacles(self) -> None:
        for obstacle in self.obstacles:
            obstacle.draw()  # Draw each obstacle

    def create_obstacle(self) -> None:
        ran = random.randint(0, 2)  # Generate a random number to determine the type of obstacle
        ranObj = random.randint(0, 2)  # Choose between obstacle car, bus, and bike
        if ranObj == 0:
            self.obstacles.append(ObstacleCar(15 + ran * 35, -30))  # Create an ObstacleCar obstacle
        elif ranObj == 1:
            self.obstacles.append(Bus(15 + ran * 35, -30))  # Create a Bus obstacle
        else:
            self.obstacles.append(Bike(15 + ran * 35, -30))  # Create a Bike obstacle

    def restart(self) -> None:
        self.car = Car()  # Reset the player's car
        self.player_speed = 1  # Reset player's speed
        self.player_position = 0  # Reset player's position
        self.score = 0  # Reset the score
        self.game_over = False  # Reset the game over flag
        self.obstacle_threshold = 50  # Reset the minimum distance between obstacles
        self.next_obstacle_position = self.obstacle_threshold  # Reset the position of the next obstacle
        self.count = 0  # Reset the animation counter
        self.obstacles = []  # Clear the list of obstacles
        threading.Thread(target=self.update_score).start()  # Start a thread to update the score in the background

    def game_over_hud(self) -> None:
        px.cls(15)  # Clear the screen with a specific color
        px.text(35, 50, "GAME OVER", 7)  # Show the game over message
        px.text(20, 60, "Press 'R' to restart", 7)  # Show the restart message
        px.text(20, 70, "Your score: " + str(self.score), 7)  # Show the player's final score

    def check_collision(self) -> bool:
        for obstacle in self.obstacles:
            if type(obstacle) == Bus:
                if self.car.x + 16 > obstacle.x and self.car.x < obstacle.x + 16 and self.car.y + 24 > obstacle.y and self.car.y < obstacle.y + 39:
                    return True  # Return True if there is a collision with a bus
            if type(obstacle) == ObstacleCar:
                if self.car.x + 16 > obstacle.x and self.car.x < obstacle.x + 16 and self.car.y + 24 > obstacle.y and self.car.y < obstacle.y + 32:
                    return True  # Return True if there is a collision with a car
            if type(obstacle) == Bike:
                if self.car.x + 16 > obstacle.x and self.car.x < obstacle.x + 16 and self.car.y + 24 > obstacle.y and self.car.y < obstacle.y + 27:
                    return True  # Return True if there is a collision with a bike
        return False  # Return False if there is no collision

App()  # Start the application
