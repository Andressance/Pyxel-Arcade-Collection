import pyxel


def press_to_start():
    # Display "Press any Key to start" message
    pyxel.text(50, 50, "Press any Key to start", 7)

def show_score(score):
    # Display current score
    pyxel.text(5, 5, "Score: " + str(score), 7)

def game_over():
    # Display "Game Over" message and "Press Space to restart" message
    pyxel.text(50, 50, "Game Over", 8)
    pyxel.text(50, 60, "Press Space to restart", 5)
