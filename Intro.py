import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=("Helvetica", 20), width=5, height=2,
                                                command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player

            if self.check_winner(row, col):
                self.show_winner()
            elif self.check_draw():
                self.show_draw()
            else:
                self.switch_player()


    def check_winner(self, row, col):
        player = self.current_player
        return (all(self.board[row][c] == player for c in range(3)) or
                all(self.board[r][col] == player for r in range(3)) or
                all(self.board[i][i] == player for i in range(3)) or
                all(self.board[i][2 - i] == player for i in range(3)))

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))


    def show_winner(self):
        winner = f"Player {self.current_player} wins!"
        messagebox.showinfo("Game Over", winner)
        self.root.quit() 

    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.root.quit()

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def play(self):
        self.root.mainloop() 

if __name__ == "__main__":
    game = TicTacToe()
    game.play()   