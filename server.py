import socket
import threading
import tkinter as tk
from tictactoe_gui import TicTacToeGUI

class TicTacToeServer:
    def __init__(self, host='localhost', port=9999):
        self.root = tk.Tk()
        self.gui = TicTacToeGUI(self.root, self.send_move)
        self.client = None
        self.player_name = self.gui.player_name
        self.host = host
        self.port = port
        threading.Thread(target=self.start_server, daemon=True).start()
        self.root.mainloop()

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(1)
        self.client, _ = server.accept()
        self.client.send(self.player_name.encode())
        opponent_name = self.client.recv(1024).decode()
        self.gui.opponent_name = opponent_name
        self.gui.scores[opponent_name] = 0
        threading.Thread(target=self.listen, daemon=True).start()

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
    TicTacToeServer()