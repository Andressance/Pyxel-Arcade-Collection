import pyxel
import hud

class App:
    def __init__(self):
        # Initialize Pyxel window
        pyxel.init(160, 120, "Tic Tac Toe")
        # Load resources and configure mouse
        pyxel.load("resources/PYXEL_RESOURCE_FILE.pyxres")
        pyxel.mouse(True)
        pyxel.mouse(False)
        self.cursor_x = 0
        self.cursor_y = 0
        self.button_hovered = False
        self.in_game = False
        self.table = [["","",""], ["","",""], ["","",""]]
        self.turn = 0
        self.symbol = "X"
        # Run Pyxel app
        self.tie = False
        pyxel.run(self.update, self.draw)
    
    def update(self):
        # Update cursor position
        self.cursor_x = pyxel.mouse_x
        self.cursor_y = pyxel.mouse_y

        # Handle game logic
        if self.in_game:    
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and not self.check_winner():
                # Check for clicks and update game state
                self.handle_click()
                # Change player turn
                self.toggle_turn()
                
            # Restart game if R key is pressed and there is a winner
            if pyxel.btnp(pyxel.KEY_R) and self.check_winner():
                self.restart()
        
        else:   
            # Check if cursor is inside the button and handle button click
            self.handle_button_click()
                
    def draw(self):
        # Clear screen
        pyxel.cls(7)
    
        if not self.in_game:
            # Draw title and start button
            hud.title()
            hud.button(55, 60, "Start Game", 0 if self.button_hovered else 8)
            pyxel.blt(self.cursor_x, self.cursor_y, 0, 40, 8, 8, 8, 0)

        else: 
            # Draw game board
            self.draw_board()
            # Check for winner and draw messages
            self.check_and_draw_winner()
            # Draw cursor
            pyxel.blt(self.cursor_x, self.cursor_y, 0, 40, 8, 8, 8, 0)

    def is_inside_button(self, x, y):
        # Check if coordinates are inside the button
        return 55 <= x <= 110 and 60 <= y <= 70

    def handle_button_click(self):
        # Handle button click
        self.button_hovered = self.is_inside_button(self.cursor_x, self.cursor_y)
        if self.button_hovered:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.in_game = True
    
    def handle_click(self):
        # Handle click on game board
        for i in range(3):
            for j in range(3):
                if self.is_inside_cell(i, j) and self.table[i][j] == "":
                    self.table[i][j] = self.symbol
                    self.turn += 1

    def toggle_turn(self):
        # Toggle player turn
        if self.turn % 2 == 0:
            self.symbol = "X"
        else:
            self.symbol = "O"

    def is_inside_cell(self, i, j):
        # Check if cursor is inside a cell
        cell_x = 50 + j * 15
        cell_y = 40 + i * 15
        return cell_x <= self.cursor_x <= cell_x + 15 and cell_y <= self.cursor_y <= cell_y + 15

    def draw_board(self):
        # Draw game board
        pyxel.blt(50, 40, 1, 0, 0, 48, 48, 1)
        for i in range(3):
            for j in range(3):
                if self.table[i][j] == "X":
                    pyxel.blt(51 + j * 15, 41 + i * 15, 0, 17, 1, 13, 13, 1)
                elif self.table[i][j] == "O":
                    pyxel.blt(51 + j * 15, 41 + i * 15, 0, 1, 1, 13, 13, 1)

    def check_and_draw_winner(self):
        # Check for winner and draw messages
        if self.check_winner():
            if not self.tie:
                hud.winner(self.symbol)
            else:
                hud.tie()
                
    def check_winner(self):
        # Check for winner
        if self.turn >= 5:
            for i in range(3):
                # Check rows
                if self.table[i][0] == self.table[i][1] == self.table[i][2] != "":
                    self.symbol = self.table[i][0]
                    return True
                # Check columns
                if self.table[0][i] == self.table[1][i] == self.table[2][i] != "":
                    self.symbol = self.table[0][i]
                    return True
            # Check diagonals
            if self.table[0][0] == self.table[1][1] == self.table[2][2] != "":
                self.symbol = self.table[0][0]
                return True
            if self.table[0][2] == self.table[1][1] == self.table[2][0] != "":
                self.symbol = self.table[0][2]
                return True
            # Check for tie
            if self.turn == 9:
                self.tie = True
                return True
        return False
    
    def restart(self):
        # Restart game
        self.in_game = False
        self.tie = False
        self.turn = 0
        self.symbol = "X"
        self.table = [["","",""], ["","",""], ["","",""]]

# Start the game
App()
