#stage1 creating tic tac toe board display

theBoard = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]


def print_board(theBoard):
    print(theBoard[0] + " | " + theBoard[1] + " | " + theBoard[2])
    print("---------")
    print(theBoard[3] + " | " + theBoard[4] + " | " + theBoard[5])
    print("---------")
    print(theBoard[6] + " | " + theBoard[7] + " | " + theBoard[8])
print_board(theBoard)