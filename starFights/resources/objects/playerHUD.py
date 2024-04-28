import pyxel as px

class PlayerHUD:
    def __init__(self, health:int, force:int, block_stamina:int, max_health:int, max_force:int, max_stamina:int):
        self.health = health
        self.force = force
        self.stamina = block_stamina
        self.MAX_HEALTH = max_health
        self.MAX_FORCE = max_force
        self.MAX_STAMINA = max_stamina

        self.health_x = 20
        self.health_y = 3
        self.health_width = 100
        self.health_height = 10

        self.force_x = 130
        self.force_y = 3

        self.stamina_x = 240
        self.stamina_y = 3

        self.force_width = 100
        self.force_height = 10

        self.INITIAL_COORDS = (1,123,0)
        self.FINAL_COORDS = (9,123,0)
        self.TAMAÑO = (6,10)

        px.load("resources/sprites/sprites.pyxres")

    def update(self, health:int, force:int, stamina:int):
        self.health = health
        self.force = force
        self.stamina = stamina

    def draw(self):
        self.draw_frame()
        self.draw_health()
        self.draw_force()
        self.draw_stamina()

    def draw_health(self):
        # Calculamos el ancho de la barra de vida llena
        filled_width = max(0, int(self.health / self.MAX_HEALTH * self.health_width) - 4)

        # Dibujamos la barra inicial
        px.blt(self.health_x, self.health_y, self.INITIAL_COORDS[2], self.INITIAL_COORDS[0], self.INITIAL_COORDS[1], self.TAMAÑO[0], self.TAMAÑO[1], 0)

        # Dibujamos la llave izquierda
        px.rect(self.health_x + self.TAMAÑO[0] - 1, self.health_y + 1, 1, self.TAMAÑO[1] - 2, 8)

        # Dibujamos la barra de vida llena
        if filled_width > 0:
            px.rect(self.health_x + self.TAMAÑO[0], self.health_y, filled_width - 1, self.TAMAÑO[1], 8)

        # Dibujamos la barra de vida vacía
        empty_width = self.health_width - self.TAMAÑO[0] - filled_width
        px.rect(self.health_x + self.TAMAÑO[0] + filled_width, self.health_y, empty_width, self.TAMAÑO[1], 2)

        if self.health == 100:
            # Dibujamos la llave derecha
            px.rect(self.health_x + self.health_width - self.TAMAÑO[0], self.health_y + 1, 1, self.TAMAÑO[1] - 2, 8)
        else:
            px.rect(self.health_x + self.health_width - self.TAMAÑO[0], self.health_y + 1, 1, self.TAMAÑO[1] - 2, 2)
        

        # Dibujamos la barra final
        px.blt(self.health_x + self.health_width, self.health_y, self.FINAL_COORDS[2], self.FINAL_COORDS[0], self.FINAL_COORDS[1], self.TAMAÑO[0], self.TAMAÑO[1], 0)

    def draw_force(self):
        # Calculamos el ancho de la barra de fuerza llena
        filled_width = max(0, int(self.force / self.MAX_FORCE * self.force_width) - 4)

        # Dibujamos la barra inicial de fuerza
        px.blt(self.force_x, self.force_y, self.INITIAL_COORDS[2], self.INITIAL_COORDS[0], self.INITIAL_COORDS[1], self.TAMAÑO[0], self.TAMAÑO[1], 0)

        # Dibujamos la llave izquierda de la barra de fuerza
        px.rect(self.force_x + self.TAMAÑO[0] - 1, self.force_y + 1, 1, self.TAMAÑO[1] - 2, 12)

        # Dibujamos la barra de fuerza llena
        if filled_width > 0:
            px.rect(self.force_x + self.TAMAÑO[0], self.force_y, filled_width - 1, self.TAMAÑO[1], 12)

        # Dibujamos la barra de fuerza vacía
        empty_width = self.force_width - self.TAMAÑO[0] - filled_width
        px.rect(self.force_x + self.TAMAÑO[0] + filled_width, self.force_y, empty_width, self.TAMAÑO[1], 5)

        # Dibujamos la llave derecha de la barra de fuerza
        if self.force == self.MAX_FORCE:
            px.rect(self.force_x + self.force_width - self.TAMAÑO[0], self.force_y + 1, 1, self.TAMAÑO[1] - 2, 12)
        else:
            px.rect(self.force_x + self.force_width - self.TAMAÑO[0], self.force_y + 1, 1, self.TAMAÑO[1] - 2, 5)

        # Dibujamos la barra final de fuerza
        px.blt(self.force_x + self.force_width, self.force_y, self.FINAL_COORDS[2], self.FINAL_COORDS[0], self.FINAL_COORDS[1], self.TAMAÑO[0], self.TAMAÑO[1], 0)

    def draw_stamina(self):
        # Calculamos el ancho de la barra de stamina llena
        filled_width = max(0, int(self.stamina / self.MAX_STAMINA * self.force_width) - 4)

        # Dibujamos la barra inicial de stamina
        px.blt(self.stamina_x, self.stamina_y, self.INITIAL_COORDS[2], self.INITIAL_COORDS[0], self.INITIAL_COORDS[1], self.TAMAÑO[0], self.TAMAÑO[1], 0)

        # Dibujamos la llave izquierda de la barra de stamina
        px.rect(self.stamina_x + self.TAMAÑO[0] - 1, self.stamina_y + 1, 1, self.TAMAÑO[1] - 2, 3)

        # Dibujamos la barra de stamina llena
        if filled_width > 0:
            px.rect(self.stamina_x + self.TAMAÑO[0], self.stamina_y, filled_width - 1, self.TAMAÑO[1], 3)

        # Dibujamos la barra de stamina vacía
        empty_width = self.force_width - self.TAMAÑO[0] - filled_width
        px.rect(self.stamina_x + self.TAMAÑO[0] + filled_width, self.stamina_y, empty_width, self.TAMAÑO[1], 11)

        # Dibujamos la llave derecha de la barra de stamina
        if self.stamina == self.MAX_STAMINA:
            px.rect(self.stamina_x + self.force_width - self.TAMAÑO[0], self.stamina_y + 1, 1, self.TAMAÑO[1] - 2, 3)
        else:
            px.rect(self.stamina_x + self.force_width - self.TAMAÑO[0], self.stamina_y + 1, 1, self.TAMAÑO[1] - 2, 11)

        # Dibujamos la barra final de stamina
        px.blt(self.stamina_x + self.force_width, self.stamina_y, self.FINAL_COORDS[2], self.FINAL_COORDS[0], self.FINAL_COORDS[1], self.TAMAÑO[0], self.TAMAÑO[1], 0)


    def draw_frame(self):
        # Show top left corner
        px.blt(0,0,0, 0, 136, 16, 22, 0)

        px.rect(16, 0, px.width - 32, 1, 9)
        px.rect(16, 1, px.width - 32, 14, 7)
        px.rect(16, 15, px.width - 32, 1, 9)

        # Show top right corner
        px.blt(px.width - 16, 0, 0, 16, 136, 16, 22, 0)



