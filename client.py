import socket
import threading
import tkinter as tk
from tictactoe_gui import TicTacToeGUI

class TicTacToeClient:
    def __init__(self, host='localhost', port=9999):
        self.root = tk.Tk()
        self.gui = TicTacToeGUI(self.root, self.send_move)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.opponent_name = self.client.recv(1024).decode()
        self.client.send(self.gui.player_name.encode())
        self.gui.opponent_name = self.opponent_name
        self.gui.scores[self.opponent_name] = 0
        threading.Thread(target=self.listen, daemon=True).start()
        self.root.mainloop()

    def send_move(self, row=None, col=None, restart=False):
        if self.client:
            if restart:
                self.client.send(b"RESTART")
            else:
                self.client.send(f"{row},{col}".encode())

    def listen(self):
        while True:
            try:
                data = self.client.recv(1024)
                if not data:
                    break
                decoded = data.decode()
                if decoded == "RESTART":
                    self.gui.receive_restart()
                else:
                    row, col = map(int, decoded.split(','))
                    self.gui.receive_move(row, col)
            except:
                break

if __name__ == "__main__":
    TicTacToeClient()
