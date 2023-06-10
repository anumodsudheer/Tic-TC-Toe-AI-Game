import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def find_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        return None
    def next_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O'\
                if self.current_player == 'X' else 'X'

root = tk.Tk()
root.title("TIC TAC TOE GAME")
match = TicTacToe()
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text=' ', width=14, height=7,command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

def button_click(row, col):
    match.next_move(row, col)
    buttons[row][col]['text'] = match.board[row][col]
    Winner = match.find_winner()
    if Winner:
        messagebox.showinfo("Game is Over", f"Player {Winner} won!")
        root.quit()
    elif all(match.board[row][col] != ' ' for row in range(3) for col in range(3)):
        messagebox.showinfo("Game Over boy", "It is a tie!")
        root.quit()

    chance_of_ai()
def chance_of_ai():
    for row in range(3):
        for col in range(3):
            if match.board[row][col] == ' ':
                match.next_move(row, col)
                buttons[row][col]['text'] = match.board[row][col]
                Winner = match.find_winner()
                if Winner:
                    messagebox.showinfo("Game is Over", f"Player {Winner} won!")
                    root.quit()
                return
root.mainloop()
