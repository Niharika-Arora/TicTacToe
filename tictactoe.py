import sys


def tac_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def menu():
    ch = input("Do you want to play? (yes or no) : ")
    if ch.casefold() == "no".casefold():
        sys.exit(0)
    elif ch.casefold() == "yes".casefold():
        print("Who goes first?")
        choice = input("Enter 'p' for player and 'c' or computer : ")
        return choice


def full(board):
    for i in range(1, 10):
        if space(board, i):
            return False
    return True


def space(board, m):
    return board[m] == ' '


def check_win(brd, let):
    return (brd[1] == let and brd[2] == let and brd[3] == let) or (
            brd[4] == let and brd[5] == let and brd[6] == let) or (
            brd[7] == let and brd[8] == let and brd[9] == let) or (
            brd[1] == let and brd[4] == let and brd[7] == let) or (
            brd[2] == let and brd[5] == let and brd[8] == let) or (
            brd[3] == let and brd[6] == let and brd[9] == let) or (
            brd[1] == let and brd[5] == let and brd[9] == let) or (
            brd[3] == let and brd[5] == let and brd[7] == let)


def move(board):
    m = input("Next move (1-9) : ")
    return int(m)


if __name__ == "__main__":
    print("******Welcome to the game of Tic Tac Toe******")
    while True:
        bord = [' ' for i in range(10)]
