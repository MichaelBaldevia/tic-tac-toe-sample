from zero import ZeroClient
import tkinter as tk
from tkinter import messagebox

zero_client = ZeroClient("localhost", 5559)
# Initialize variables
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1

window = tk.Tk()
window.title("Tic Tac Toe")


class RpcClient:
    def __init__(self, zero_client: ZeroClient):
        self._zero_client = zero_client
    def echo(self, msg: str) -> str:
        return self._zero_client.call("echo", msg)
    # Declare the winner and ask to restart the games
    def declare_winner(winner: str) -> str:
        if winner == "tie":
            message = "It's a tie!"
        else:
            message = f"Game Over. Player {winner} wins!"
        return message

class TicTacToe:
# Check for a winner or a tie
    def check_for_winner():
        winner = None

        # Check rows
        for row in board:
            if row.count(row[0]) == len(row) and row[0] != 0:
                winner = row[0]
                break

        # Check columns
        for col in range(len(board)):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
                winner = board[0][col]
                break

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
            winner = board[0][0]
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
            winner = board[0][2]

        if all([all(row) for row in board]) and winner is None:
            winner = "tie"

        if winner:
            print(RpcClient.declare_winner(winner))
            window.quit()

    # Handle button clicks
    def handle_click(row, col):
        global current_player
        if board[row][col] == 0:
            if current_player == 1:
                board[row][col] = "X"
                current_player = 2
            else:
                board[row][col] = "O"
                current_player = 1

            button = window.grid_slaves(row=row, column=col)[0]
            button.config(text=board[row][col])

            TicTacToe.check_for_winner()

    
