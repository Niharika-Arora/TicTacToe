def tac_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def check_win(brd, let):
    return (brd[1] == let and brd[2] == let and brd[3] == let) or (brd[4] == let and brd[5] == let and brd[6] == let) or (brd[7] == let and brd[8] == let and brd[9] == let) or (brd[1] == let and brd[4] == let and brd[7] == let) or (brd[2] == let and brd[5] == let and brd[8] == let) or (brd[3] == let and brd[6] == let and brd[9] == let) or (brd[1] == let and brd[5] == let and brd[9] == let) or (brd[3] == let and brd[5] == let and brd[7] == let)


if __name__ == "__main__":
    print("******Welcome******")
    while True:
        board = [' ' for i in range(10)]