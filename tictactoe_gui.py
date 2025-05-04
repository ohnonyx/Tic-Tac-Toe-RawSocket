import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

class TicTacToeGUI:
    def __init__(self, root, send_callback, player_name=None):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("650x1000")

        bg_image = Image.open("background.jpg")
        bg_image = bg_image.resize((650, 1000))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.player_name = player_name or simpledialog.askstring("Name", "Enter your name:")
        self.symbol_style = simpledialog.askstring("Style", "Choose symbol style:\n1. Emoji 😺/🐶\n2. Classic X/O\n3. Moon and stars 🌙/🌟\n4. Hearts and bows ❤/🎀", initialvalue="1")
        if self.symbol_style == "4":
            self.emoji_map = {"X": "❤", "O": "🎀"}
        elif self.symbol_style == "3":
            self.emoji_map = {"X": "🌙", "O": "🌟"}
        elif self.symbol_style == "2":
            self.emoji_map = {"X": "X", "O": "O"}
        else:
            self.emoji_map = {"X": "😺", "O": "🐶"}

        self.symbol = None
        self.opponent_symbol = None
        self.first_move_made = False
        self.board = [[" "]*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.turn = None
        self.counter = 0
        self.game_over = False
        self.winner = None
        self.send_callback = send_callback
        self.opponent_name = "Opponent"
        self.scores = {self.player_name: 0, self.opponent_name: 0}

        self.status_label = tk.Label(self.root, text="Waiting...", font=("Arial", 16, "bold"), bg="#5c45ba", fg="#6A5ACD")
        self.status_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), bg="#5c45ba", fg="#333")
        self.score_label.pack()

        board_frame = tk.Frame(self.root, bg="#6a5acd")
        board_frame.pack()
        self.create_board(board_frame)

        self.restart_btn = tk.Button(self.root, text="🔄 Restart Game", font=("Arial", 12, "bold"), bg="#E0BBE4", fg="#4B0082", command=self.restart_button_clicked)
        self.restart_btn.pack(pady=10)

        self.update_status()
        self.update_scoreboard()

    def create_board(self, frame):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(frame, text=" ", font=("Arial", 40), width=5, height=2,
                                bg="#d9c8fa", fg="#8B5E83", activebackground="#E6E6FA", activeforeground="#8B5E83",
                                command=lambda r=row, c=col: self.cell_clicked(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = btn

    def update_status(self):
        if self.game_over:
            return
        if not self.symbol:
            self.status_label.config(text="Game starts when anyone clicks first", fg="#c5abf5")
        elif self.turn == self.symbol:
            self.status_label.config(text=f"Your turn ({self.player_name})")
        else:
            self.status_label.config(text=f"Waiting for {self.opponent_name}...")

    def update_scoreboard(self):
        score_text = f"{self.player_name} : {self.scores[self.player_name]}   |   {self.opponent_name} : {self.scores[self.opponent_name]}"
        self.score_label.config(text=score_text, fg="#c5abf5")

    def cell_clicked(self, row, col):
        if self.board[row][col] != " " or self.game_over:
            return
        if not self.first_move_made:
            self.symbol = "X"
            self.opponent_symbol = "O"
            self.turn = "X"
            self.first_move_made = True
        if self.turn != self.symbol:
            return
        self.send_callback(row, col)
        self.apply_move(row, col, self.symbol)
        self.turn = self.opponent_symbol
        self.update_status()

    def apply_move(self, row, col, player_symbol):
        self.board[row][col] = player_symbol
        emoji = self.emoji_map[player_symbol]
        color = "#FF69B4" if player_symbol == "X" else "#87CEFA"
        self.buttons[row][col].config(text=emoji, state="disabled", disabledforeground=color)
        self.counter += 1
        if self.check_if_won():
            self.game_over = True
            winner_name = self.player_name if self.winner == self.symbol else self.opponent_name
            self.scores[winner_name] += 1
            self.update_scoreboard()
            self.status_label.config(text=f"{winner_name} wins! 🎉")
            messagebox.showinfo("Game Over", f"{winner_name} wins! 🎉")
        elif self.counter == 9:
            self.game_over = True
            self.status_label.config(text="It's a tie! 🤝")
            messagebox.showinfo("Game Over", "It's a tie! 🤝")

    def check_if_won(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != " ":
                self.winner = b[i][0]
                return True
            if b[0][i] == b[1][i] == b[2][i] != " ":
                self.winner = b[0][i]
                return True
        if b[0][0] == b[1][1] == b[2][2] != " ":
            self.winner = b[0][0]
            return True
        if b[0][2] == b[1][1] == b[2][0] != " ":
            self.winner = b[0][2]
            return True
        return False

    def receive_move(self, row, col):
        if not self.first_move_made:
            self.symbol = "O"
            self.opponent_symbol = "X"
            self.turn = "X"
            self.first_move_made = True
        self.apply_move(row, col, self.opponent_symbol)
        self.turn = self.symbol
        self.update_status()

    def receive_restart(self):
        self.reset_game()

    def reset_game(self):
        self.board = [[" "]*3 for _ in range(3)]
        self.counter = 0
        self.winner = None
        self.game_over = False
        self.first_move_made = False
        self.symbol = None
        self.opponent_symbol = None
        self.turn = None
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ", state="normal")
        self.update_status()

    def restart_button_clicked(self):
        self.send_callback(restart=True)
        self.reset_game()