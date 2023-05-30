import pyfiglet
import random
import time
import os
from termcolor import colored

os.system('color')

title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

#Menu
print("Press 1 to select Player vs computer mode.")
print("Press 2 tp select Player vs Player mode.")
key = int(input("Enter your choice:"))

if key == 1:
    print("*** Player vs CPU mode ***")
elif key == 2:
    print("*** Player vs Player mode ***")
else:
    print("*** Wrong input... Try again ***")
    exit()

start_game_time = time.time()

def show():
    for row in game_board:
        for col in row:
            print(col, end=" ")
        print()


def check_game():
    # This function check if any player in winning
    winner = False

    # Check the rows
    for row in range(0, 3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] == "X":
            winner = True
            if key == 2:
                print("Player 1 wins the game.")
            else:
                print("Player wins the game.")

        elif game_board[row][0] == game_board[row][1] == game_board[row][2] == "O":
            winner = True

            if key == 2:
                print("Player 2 wins the game.(in rows)")
            else:
                print("Computer wins the game.")

    # Check the columns
    for col in range(0, 3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] == "X":
            winner = True
            if key == 2:
                print("Player 1 wins the game.")
            else:
                print("Player wins the game.")

        elif game_board[0][col] == game_board[1][col] == game_board[2][col] == "O":
            winner = True
            if key == 2:
                print("Player 2 wins the game.(in cols)")
            else:
                print("Computer wins the game.")

    # Check the diagnoals
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == "X":
        winner = True
        if key == 2:
            print("Player 1 wins the game.")
        else:
            print("Player wins the game.")

    elif game_board[0][0] == game_board[1][1] == game_board[2][2] == "O":
        winner = True

        if key == 2:
            print("Player 2 wins the game.(in left to right diag)")
        else:
            print("Computer wins the game.")

    elif game_board[0][2] == game_board[1][1] == game_board[2][0] == "X":
        winner = True
        if key == 2:
            print("Player 1 wins the game.")
        else:
            print("Player wins the game.")

    elif game_board[0][2] == game_board[1][1] == game_board[2][0] == "O":
        winner = True

        if key == 2:
            print("Player 2 wins the game.(in right to left diag)")
        else:
            print("Computer wins the game.")

    elif not any("_" in i for i in game_board):
        winner = True
        print("The game is draw... No one wined the game.")

    return winner


game_board = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]]

show()

if key == 1:
    while True:
        print("Player")

        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if (0 <= row <= 2) and (0 <= col <= 2):
                if game_board[row][col] == "_":
                    game_board[row][col] = colored("X", "red", attrs=["bold"])
                    break
                else:
                    print("...This cell is full...")
            else:
                print("Your row or column number are wrong and out of range.")

        show()
        if check_game():
            break

        print("CPU")

        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if game_board[row][col] == '_':
                game_board[row][col] = colored("O", "blue", attrs=["bold"])
                break
            else:
                print("...Computer entered a position that is full...")

        show()
        if check_game():
            break


elif key == 2:
    while True:
        print("Player 1")

        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if (0 <= row <= 2) and (0 <= col <= 2):
                if game_board[row][col] == "_":
                    game_board[row][col] = colored("X","red", attrs=["bold"])
                    break
                else:
                    print("...This cell is full...")
            else:
                print("Your row or column number are wrong and out of range.")

        show()
        if check_game():
            break

        print("Player 2")

        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if (0 <= row <= 2) and (0 <= col <= 2):
                if game_board[row][col] == '_':
                    game_board[row][col] = colored("O", "blue", attrs=["bold"])
                    break
                else:
                    print("...This cell is full...")
            else:
                print("Your row or column number are wrong and out of range.")
        show()
        if check_game():
            break

end_game_time = time.time()
game_total_time = end_game_time - start_game_time

print("Game duration was ", game_total_time, " seconds")

