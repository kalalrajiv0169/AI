#p9
import random
# Initialize board
board = [" " for _ in range(9)]

# Function to print the board

def print_board():
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i+1] + "|" + board[i+2])
# Function to handle player's move

def player_move():
    move = int(input("Enter your position (0-8): "))
    if board[move] == " ":
        board[move] = "X"
# Function to handle AI's move

def ai_move():
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"
    
# Game loop
while " " in board:
    print_board()
    player_move()
    if " " not in board:
        break
    ai_move()

print_board()
print("Game over")
