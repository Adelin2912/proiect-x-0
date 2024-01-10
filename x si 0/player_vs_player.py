from tkinter import *
from tkinter import messagebox
from helper import *


# Initialize the game board to play with another player
def player_versus_player(game_board):
    game_board.destroy()  # destroy old gameboard and create a new one
    game_board = Tk()
    game_board.title("X si 0")  # set gameboard title

    top_button_1 = Button(game_board, text="Jucator 1 : X", width=10)
    top_button_1.grid(row=1, column=1)

    top_button_2 = Button(game_board, text="Jucator 2 : O", width=10, state=DISABLED)
    top_button_2.grid(row=2, column=1)

    generate_gameboard_with_player(game_board, top_button_1, top_button_2)


# Create the GUI when playing against another player
def generate_gameboard_with_player(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            button[i][j] = Button(game_board, bd=5, height=4, width=8)
            button[i][j].config(command=lambda i=i, j=j: get_button_text_with_players(i, j, game_board, l1, l2))
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Change text on button while playing with another player
def get_button_text_with_players(i, j, gameboard, top_button_1, top_button_2):
    global player_index
    if board[i][j] == ' ': # check if button can be marked
        # switch between player symbols based on their turn
        if player_index % 2 == 0:
            top_button_1.config(state=DISABLED)
            top_button_2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            top_button_2.config(state=DISABLED)
            top_button_1.config(state=ACTIVE)
            board[i][j] = "O"

        player_index += 1
        button[i][j].config(text=board[i][j])

    # check if, by marking current button, player has won
    if check_winner(board, "X"):
        gameboard.destroy()
        messagebox.showinfo("Castigator", "Jucatorul 1 a castigat")
    elif check_winner(board, "O"):
        gameboard.destroy()
        messagebox.showinfo("Castigator", "Jucatorul 2 a castigat")
    elif is_board_full():
        gameboard.destroy()
        messagebox.showinfo("Egalitate", "Egalitate")