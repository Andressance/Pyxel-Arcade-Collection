import pyxel

def show_score(p1, p2):
    # Display player 1 score
    pyxel.text(80, 0, f"Player 1: {p1}", 7)

def counter(count):
    # Display count
    pyxel.text(70, 0, f"Count: {count}", 7)

def game_over(): 
    # Display game over message
    pyxel.text(45, 55, "Game Over", 8)
    pyxel.text(45, 80, "Press Space to Replay", 8)

def press_to_play():
    # Display "Press Space to Play" message
    pyxel.text(40, 55, "Press Space to Play", 8)
