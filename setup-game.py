from my_client.rpc_client import RpcClient, zero_client, window, tk, TicTacToe


client = RpcClient(zero_client)

# Create board
def create_board():
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="", font=("Arial", 50), height=2, width=6, bg="lightblue", command=lambda row=i, col=j: TicTacToe.handle_click(row, col))
            button.grid(row=i, column=j, sticky="nsew")

if __name__ == "__main__":
    create_board()
    window.mainloop()