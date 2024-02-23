import pyxel

def title():
    # Draw title text
    pyxel.text(55, 41, "Tic Tac Toe", 0)

def button(x, y, text, color):
    # Draw button outline
    pyxel.rectb(x, y, x , 10, color)
    # Draw button text
    pyxel.text(x + 5, y + 2, text, color)

def turn(letter):
    # Draw current player's turn
    pyxel.text(20, 80, f"Turn: {letter}", 0)

def winner(letter):
    # Draw winner message
    pyxel.text(20, 100, f"{letter} wins!", 0)
    pyxel.text(20, 110, "Press R to restart", 0)

def tie():
    # Draw tie message
    pyxel.text(20, 100, "It's a tie!", 0)
    pyxel.text(20, 110, "Press R to restart", 0)
