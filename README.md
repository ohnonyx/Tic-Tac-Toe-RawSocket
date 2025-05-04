# 🎮 Tic Tac Toe Using Raw Sockets (2-Player)

A fun and interactive two-player network-based **Tic Tac Toe** game using **Python** and **Tkinter**, featuring a customizable emoji-based GUI and **TCP** client-server communication!

---

## 🧠 Features

- 🖧 Real-time two-player gameplay using raw socket communication (TCP)
- 🎨 Emoji and styled symbol support (😺/🐶, ❤/🎀, 🌙/🌟, or classic X/O)
- 🧑‍🤝‍🧑 Track player names and keep scores
- 🖼️ Custom themed GUI with optional background image
- 🔄 In-game restart option
- ⚡ Responsive interface using `Tkinter` and `Pillow`

---
## 🕶️ How It Looks
![WhatsApp Image 2025-05-04 at 11 28 02_5d96c8a0](https://github.com/user-attachments/assets/92e82a0e-91e7-47a7-a0e0-bc93a192eac0)

---

## 🔧 Requirements

- Python 3.x
- Pillow library (`pip install pillow`)
- Two computers on the same network (LAN) or use localhost for testing
- Open port `9999` on both machines

---

## 📁 Project Files

- `server.py` – Run by **Player 1 (Host)**
- `client.py` – Run by **Player 2 (Client)** - make sure to change the host details to the host IP address
- `tictactoe_gui.py` – GUI logic shared by both server and client
- `background.jpg` – Background image used in the GUI - you can change this image but make sure to resize it in tictactoe_gui.py

---

## 🕹 How to Play (2-Player Setup)

### 👤 Player 1 – Host
1. Open a terminal and run:
   ```bash
   python server.py
2. Enter your name and choose your emoji/symbol style from the prompt.
3. Wait for Player 2 to connect.
4. Once Player 2 joins, the game starts.

### 👤 Player 2 – Client
1. Open client.py in a code editor.
2. Change the IP address of HOST to Player 1’s IP:
   ```bash
   self.client.connect(('192.168.X.X', 9999))  # Replace with host IP
3. Open terminal and run: 
   ```bash
   python client.py
4. Enter your name and emoji style.
5. Game begins once connected.

---

## 🎮 Gameplay Rules
- Players take turns clicking grid buttons to place their symbols.
- First player to align 3 symbols (row, column, or diagonal) wins.
- Game detects win/tie conditions and displays result.
- Scoreboard updates automatically.
- Restart anytime using the “🔄 Restart Game” button — syncs with opponent.

---

## 🤝 Authors
- Nishita Singh (https://github.com/ohnonyx)
- Nithya Prashaanthi R. (https://github.com/nithya-1385/)
