import pyxel

class Button:
    def __init__(self, x, y, w, h, text, color_text, border_color, circle:bool ,blank:bool, hovered_text_color=None,hovered_color=None) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color_text = color_text
        self.border_color = border_color
        self.circle = circle
        self.hovered_text_color = hovered_text_color
        self.hovered_color = hovered_color
        self.blank = blank
        self.clicked = False
        
    def update(self) -> None:
        if self.hovered() and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.clicked = True
            pyxel.mouse(False)
        
    def draw(self) -> None:
        # Set text color based on hover state
        text_color = self.hovered_text_color if self.hovered() and self.hovered_text_color is not None else self.color_text

        # Calculate approximate text width based on text length
        text_width = len(self.text) * 4  # Estimating text width, can be adjusted based on font size

        if self.circle:
            center = ((self.x + self.w) / 2, (self.y + self.h) / 2)
            if self.w == self.h:
                if self.blank:
                    pyxel.circb(self.x, self.y, self.w, self.border_color)
                else:
                    pyxel.circ(self.x, self.y, self.w, self.border_color)
            else:
                if self.blank:
                    pyxel.ellib(self.x, self.y, self.w, self.h, self.border_color)
                else:
                    pyxel.elli(self.x, self.y, self.w, self.h, self.border_color)

            # Calculate text position to center it horizontally and vertically within the circle button
            text_x = self.x + (self.w - text_width) // 2  # Center text horizontally
            text_y = self.y + (self.h - 6) // 2  # Center text vertically, manual adjustment for font size
        else:
            if self.blank:
                pyxel.rectb(self.x, self.y, self.w, self.h, self.border_color)
            else:
                pyxel.rect(self.x, self.y, self.w, self.h, self.border_color)

            # Calculate text position to center it horizontally and vertically within the rectangular button
            text_x = self.x + (self.w - text_width) // 2  # Center text horizontally
            text_y = self.y + (self.h - 6) // 2  # Center text vertically, manual adjustment for font size

        # Render the text with calculated position and color
        pyxel.text(text_x, text_y, self.text, text_color)

    def hovered(self) -> bool:
        if not self.circle:
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            return self.x < mx < self.x + self.w and self.y < my < self.y + self.h
        else:
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            center_x = self.x + self.w / 2
            center_y = self.y + self.h / 2
            return ((mx - center_x) ** 2) / ((self.w / 2) ** 2) + ((my - center_y) ** 2) / ((self.h / 2) ** 2) <= 1