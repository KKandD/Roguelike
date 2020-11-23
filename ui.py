def display_board(board = list()):
    for row in board:
        for col in row:
            print(col, end="")
        print()
