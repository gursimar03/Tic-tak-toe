# ---glob var---
game_on = True
winner = None
curr_player = "X"

# ---board---
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]


def display():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play():
    display()
    while game_on:
        handle_turn(curr_player)
        check_over()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")


def handle_turn(player):
    global curr_player
    print(curr_player + "'s Turn")
    post = input("choose a position from 1 to 9: ")
    while post not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", ]:
        post = input("Invalid Input. choose a position from 1 to 9: ")
    post = int(post) - 1
    if curr_player == "X" and board[post] == "-":
        board[post] = "X"
        curr_player = "O"
    elif curr_player == "O" and board[post] == "-":
        board[post] = "O"
        curr_player = "X"
    else:
        print("Error: Space not free. ")
    display()


def check_over():
    check_win()
    check_tie()


def check_win():
    global winner
    # checkrows
    row_winner = check_rows()
    # checkcolomns
    colm_winner = check_colm()
    # checkdiagonals
    diag_winner = check_diag()
    if row_winner:
        # there is a winner
        winner = row_winner
    elif diag_winner:
        # there is a winner
        winner = diag_winner
    elif colm_winner:
        # there is a winner
        winner = colm_winner
    else:
        # there is no winner
        winner = None
    return


def check_rows():
    global game_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_colm():
    global game_on
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[2] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_on = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diag():
    global game_on
    diag_1 = board[0] == board[4] == board[7] != "-"
    diag_2 = board[2] == board[4] == board[5] != "-"
    if diag_1 or diag_2:
        game_on = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return


def check_tie():
    global game_on
    if "-" not in board:
        game_on = False
    return


play()

# display board
# play game
# check win
# check row
# check coloms
# check diagonals
# board
# check tie
# flip player
# handle turn