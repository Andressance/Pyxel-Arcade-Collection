import pyxel as px
from resources.hud.UI_Components.Button import Button
from time import sleep
from resources.hud.settings import Settings



class Hud:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.main_menu_open = False
        self.appear_speed = 10  # Velocidad de aparición de la animación
        self.appear_progress = 0  # Progreso de la animación de aparición
        self.animation_finished = False
        self.in_settings = False
        self.main_menu_x = self.x_size
        self.menu_selection = 0
        self.elections = ["START GAME", "SETTINGS", "EXIT"]
        self.main_button = Button(195, 180, 105, 10, "PRESS THE BUTTON TO START", 7, 7, False, True, 10, 10)
        self.in_game = False
        self.settings = Settings()
        px.load("resources/sprites/sprites.pyxres")
        px.mouse(True)

    def update(self):
        if not self.main_button.clicked:
            self.main_button.update()
        if self.main_button.clicked:
            self.main_menu_open = True
        if self.main_menu_open and not self.in_settings:
            self.update_main_menu()
        if self.in_settings:
            self.settings.update_settings_options()
            self.settings.update_category()
            

    def draw(self):
        if not self.main_button.clicked:
            self.draw_first_menu()
        if self.main_menu_open and not self.in_settings:
            self.animation_finished = self.appear_animation()
            self.draw_main_menu()
        if self.animation_finished and not self.in_settings:
            self.show_main_menu()
        if self.in_settings :
            self.draw_main_menu()
            self.settings.show_settings_options()
            self.settings.draw_category()
            self.in_settings =  not self.check_exit_settings()
            
            

    def draw_first_menu(self):
        
        px.bltm(0, 0, 0, 700, 460, self.x_size, self.y_size, None)
        self.main_button.draw()

    def draw_main_menu(self):
        px.bltm(0, 0, 0, 700, 460, self.x_size, self.y_size, None)

    def show_main_menu(self):
        for i, election in enumerate(self.elections):
            length = 40 if i == 0 else 33 if i == 1 else 18
            if i == self.menu_selection:
                px.rectb(209, 189 + i * 10, length, 7, 13)
                px.text(210, 190 + i * 10, election, 10)
            else:
                px.text(210, 190 + i * 10, election, 9)

    def update_main_menu(self):
        if px.btnp(px.KEY_DOWN):
            self.menu_selection += 1
            if self.menu_selection >= len(self.elections):
                self.menu_selection = 0
        if px.btnp(px.KEY_UP):
            self.menu_selection -= 1
            if self.menu_selection < 0:
                self.menu_selection = len(self.elections) - 1

        if px.btnp(px.KEY_RIGHT):
            if self.menu_selection == 0:
                self.in_game = True
            elif self.menu_selection == 1:
                self.in_settings = True
            elif self.menu_selection == 2:
                px.quit()

    def appear_animation(self):
        # Calcula el progreso de la animación
        self.appear_progress += self.appear_speed

        # Limita el progreso al tamaño de la pantalla
        self.appear_progress = min(self.appear_progress, self.x_size)

        # Dibuja la animación
        px.clip(self.x_size / 2 - self.appear_progress / 2, self.y_size / 2 - self.appear_progress / 2,
                self.appear_progress, self.appear_progress)

        # Reinicia el área de recorte si la animación está completa
        if self.appear_progress >= self.x_size:
            px.clip()
            return True
        
        return False
    
    def check_exit_settings(self):
        if self.settings.exit:
            self.settings.exit = False
            return True
        return False
    

