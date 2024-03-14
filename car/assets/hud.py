import pyxel as px

def show_score(score):
    px.text(5, 5, f"Score: {score}", 0)  # Display the player's score at (5, 5) with color 0

def display_hud():
    px.rect(0, 2, 128, 15, 0)  # Draw a rectangle for the HUD background
    px.rect(0, 0, 128, 15, 7)   # Draw a rectangle for the HUD header
