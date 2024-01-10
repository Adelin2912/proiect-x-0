import random

# Creates an empty board
board = [[" " for x in range(3)] for y in range(3)]
# sign variable to decide the turn of which player
player_index = 0


# Check the board is full or not
def is_board_full():
    full_table = True
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == ' ':
                full_table = False
                break
    return full_table


# Decide the next move of system
def computer_turn():
    empty_position = get_empty_positions()
    if len(empty_position) == 0:
        return
    else:
        return random.choice(empty_position)  # choose a random position from available moves


# verify which positions are empty on the board
def get_empty_positions():
    empty_position = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                empty_position.append([i, j])
    return empty_position


# Check if there is line of X or O on the board, so that a player wins
def check_winner(board_param, sign):
    return (
            # check on first row horizontal
            (board_param[0][0] == sign and board_param[0][1] == sign and board_param[0][2] == sign) or
            # check on second row horizontal
            (board_param[1][0] == sign and board_param[1][1] == sign and board_param[1][2] == sign) or
            # check on third row horizontal
            (board_param[2][0] == sign and board_param[2][1] == sign and board_param[2][2] == sign) or
            # check on first row vertical
            (board_param[0][0] == sign and board_param[1][0] == sign and board_param[2][0] == sign) or
            # check on second row vertical
            (board_param[0][1] == sign and board_param[1][1] == sign and board_param[2][1] == sign) or
            # check on third row vertical
            (board_param[0][2] == sign and board_param[1][2] == sign and board_param[2][2] == sign) or
            # check on principal diagonal
            (board_param[0][0] == sign and board_param[1][1] == sign and board_param[2][2] == sign) or
            # check on secondary diagonal
            (board_param[0][2] == sign and board_param[1][1] == sign and board_param[2][0] == sign)
    )
