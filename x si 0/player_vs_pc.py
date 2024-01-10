from tkinter import *
from tkinter import messagebox
from helper import *


# Initialize the game board to play with system
def player_versus_pc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("X si 0")

    l1 = Button(game_board, text="Jucator : X", width=10)
    l1.grid(row=1, column=1)

    l2 = Button(game_board, text="Computer : O", width=10, state=DISABLED)
    l2.grid(row=2, column=1)

    generate_board_with_pc(game_board, l1, l2)


# Create the GUI of game when playing against computer
def generate_board_with_pc(game_board, l1, l2):
    global buttons  # button is global and will be referenced in other functions
    buttons = []
    for i in range(3):  # generate 3 rows for grid
        m = 3 + i
        buttons.append(i)
        buttons[i] = []
        for j in range(3):  # generate 3 buttons for each row
            n = j
            buttons[i].append(j)
            buttons[i][j] = Button(game_board, bd=5, height=4, width=8)
            buttons[i][j].config(command=lambda i=i, j=j: get_button_text_with_computer(i, j, game_board, l1, l2))
            buttons[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Configure text on button while playing with system
def get_button_text_with_computer(i, j, gameboard, top_button_x, top_button_0):
    global player_index
    if board[i][j] == ' ':
        if player_index % 2 == 0:
            top_button_x.config(state=DISABLED)
            top_button_0.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            buttons[i][j].config(state=ACTIVE)
            top_button_0.config(state=DISABLED)
            top_button_x.config(state=ACTIVE)
            board[i][j] = "O"
        player_index += 1
        buttons[i][j].config(text=board[i][j])
    x = True
    if check_winner(board, "X"):
        gameboard.destroy()
        x = False
        messagebox.showinfo("Castigator", "Jucatorul a castigat")
    elif check_winner(board, "O"):
        gameboard.destroy()
        x = False
        messagebox.showinfo("Castigator", "Computer-ul a castigat")
    elif is_board_full():
        gameboard.destroy()
        x = False
        messagebox.showinfo("Egalitate", "Egalitate")
    if x:
        if player_index % 2 != 0:
            move = computer_turn()
            buttons[move[0]][move[1]].config(state=DISABLED)
            get_button_text_with_computer(move[0], move[1], gameboard, top_button_x, top_button_0)