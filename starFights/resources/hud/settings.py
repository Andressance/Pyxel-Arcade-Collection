import pyxel as px
import pyautogui

class Settings:
    def __init__(self):
        # Default settings
        self.exit = False
        self.music = True
        self.sound_effects = True
        self.fullscreen = False
        self.fps_count = False
        self.volume_effects = 50
        self.volume_music = 50
        self.graphics = 0

        self.music_options = ["ENABLE MUSIC", "ENABLE SOUND EFFECTS", "VOLUME MUSIC", "VOLUME EFFECTS", "EXIT"]
        self.graphic_options = ["GRAPHICS", "FULLSCREEN", "FPS COUNT", "EXIT"]
        self.graphic_types = ["PIXELATED", "SMOOTH", "RETRO"]
        self.categories = ["MUSIC", "GRAPHICS"]

        self.category = 0
        self.category_selection = 0

        
    '''This funcion displays graphic and music logo categories'''
    def show_settings_options(self):
        px.blt(210, 190, 0, 18, 100, 11, 10, 0)
        px.blt(230, 190, 0, 1, 100, 11, 7, 0)

    '''This function draws the settings '''
    def update_settings_options(self):
        if self.category == 0:
            self.draw_category()

    '''This function shows settings options'''
    def draw_category(self):
        if self.category == 0:  # Si la categoría es gráficos
            # Linea para subrayar la categoría seleccionada
            px.line(210, 205, 221, 205, 10)
            for i, option in enumerate(self.graphic_options):
                length = 36 if i == 0 else 40 if i == 1 else 37 if i == 2 else 16
                if i == self.category_selection:
                    px.rectb(209, 209 + i * 10, length, 7, 13)
                    px.text(210, 210 + i * 10, option, 10)
                else:
                    px.text(210, 210 + i * 10, option, 9)
        else:  # Si la categoría es música
            # Linea para subrayar la categoría seleccionada
            px.line(230, 205, 241, 205, 10)
            for i, option in enumerate(self.music_options):
                length = 49 if i == 0 else 82 if i == 1 else 49 if i == 2 else 57 if i == 3 else 16
                if i == self.category_selection:
                    px.rectb(209, 209 + i * 10, length, 7, 13)
                    px.text(210, 210 + i * 10, option, 10)
                else:
                    px.text(210, 209 + i * 10, option, 9)

    '''This function updates the category and category selection'''
    def update_category(self):
        if px.btnp(px.KEY_E):
            self.category += 1
        if px.btnp(px.KEY_Q):
            self.category -= 1

        if px.btnp(px.KEY_DOWN):
            self.category_selection += 1
            if self.category_selection >= len(self.music_options):
                self.category_selection = 0
        
        if px.btnp(px.KEY_UP):
            self.category_selection -= 1
            if self.category_selection < 0:
                self.category_selection = len(self.music_options) - 1

        if px.btnp(px.KEY_RIGHT):
            if self.category == 0:
                if self.category_selection == 0:
                    pyautogui.hotkey('alt', '9')
                    self.graphics += 1
                    if self.graphics >= len(self.graphic_types):
                        self.graphics = 0
                elif self.category_selection == 1:
                    pyautogui.hotkey('alt', 'Enter')
                    self.fullscreen = not self.fullscreen
                elif self.category_selection == 2:
                    pyautogui.hotkey('alt', '0')
                    self.fps_count = not self.fps_count
                elif self.category_selection == 3:
                    
                    self.category = 0
                    self.category_selection = 0
                    self.exit = True

            elif self.category == 1:
                if self.category_selection == 0:
                    print("ENABLE MUSIC")
                elif self.category_selection == 1:
                    print("ENABLE SOUND EFFECTS")
                elif self.category_selection == 2:
                    print("VOLUME MUSIC")
                elif self.category_selection == 3:
                    print("VOLUME EFFECTS")
                elif self.category_selection == 4:
                    
                    self.category = 0
                    self.category_selection = 0
                    self.exit = True


        # Asegurarse de que la categoría no sea menor que 0
        if self.category < 0:
            self.category = len(self.categories) - 1

        # Asegurarse de que la categoría no sea mayor o igual que la cantidad de categorías
        if self.category >= len(self.categories):
            self.category = 0

    