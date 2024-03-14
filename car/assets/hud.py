import pyxel as px

def show_score(score):
    px.text(5, 5, f"Score: {score}", 0)

def display_hud():
    px.rect(0, 2, 128, 15, 0)
    px.rect(0, 0, 128, 15, 7)