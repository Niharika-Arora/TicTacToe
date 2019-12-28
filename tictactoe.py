import sys
import random


moves = list(int(i) for i in '1 2 3 4 5 6 7 8 9'.split(" "))
corners = [1, 3, 7, 9]
sides = [2, 4, 6, 8]
center = 5


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


def first(ch):
    if ch == "p":
        let = "player"
    else:
        let = "computer"
    return let


def letter(s):
    if s == "player":
        return ['X', 'O']
    else:
        return ['O', 'X']


def full(board):
    for i in range(1, 10):
        if space(board, i):
            return False
    return True


def space(board, m):
    if board[m] == ' ':
        return True
    else:
        return False


def check_win(brd, let):
    return (brd[1] == let and brd[2] == let and brd[3] == let) or (
            brd[4] == let and brd[5] == let and brd[6] == let) or (
                   brd[7] == let and brd[8] == let and brd[9] == let) or (
                   brd[1] == let and brd[4] == let and brd[7] == let) or (
                   brd[2] == let and brd[5] == let and brd[8] == let) or (
                   brd[3] == let and brd[6] == let and brd[9] == let) or (
                   brd[1] == let and brd[5] == let and brd[9] == let) or (
                   brd[3] == let and brd[5] == let and brd[7] == let)


def move_play(board):
    m = 0
    while not space(board, m) or m not in moves:
        m = int(input("Next move (1-9) : "))
    return m


def move_comp(board, let, m):
    board[m] = let


def random_move(board, l):
    dup = list()
    for i in l:
        if space(board, i):
            dup.append(i)
    if len(dup) == 0:
        return None
    else:
        return random.choice(dup)


def duplicate(board):
    dup = list()
    for i in board:
        dup.append(i)
    return dup


def computer(board, turn):
    for i in range(1, 10):
        dup1 = duplicate(board)
        if space(dup1, i):
            move_comp(dup1, turn, i)
            if check_win(dup1, turn):
                return i
    if turn == 'X':
        p = 'O'
    else:
        p = 'X'
    for i in range(1, 10):
        dup2 = duplicate(board)
        if space(dup2, i):
            move_comp(dup2, p, i)
            if check_win(dup2, p):
                return i
    m1 = random_move(board, corners)
    if m1 is not None:
        return m1
    if space(board, center):
        return center
    m2 = random_move(board, sides)
    if m2 is not None:
        return m2


if __name__ == "__main__":
    print("******Welcome to the game of Tic Tac Toe******")
    while True:
        bord = [' ' for i in range(10)]
        c = menu()
        choice = first(c)
        player, cmp = letter(choice)
        tac_board(bord)
        game = True
        while game:
            if choice == "player":
                play = move_play(bord)
                move_comp(bord, player, play)
                if check_win(bord, player):
                    tac_board(bord)
                    print("OH NO! You've beaten me! *_*")
                    game = False
                else:
                    if full(bord):
                        tac_board(bord)
                        print("Great! You're as smart as me.")
                        break
                    else:
                        choice = "computer"
            else:
                comp = computer(bord, cmp)
                move_comp(bord, cmp, comp)
                tac_board(bord)
                if check_win(bord, cmp):
                    tac_board(bord)
                    print("Ha ha ha ha ha! Looks like you couldn't beat me! *_*")
                    game = False
                else:
                    if full(bord):
                        tac_board(bord)
                        print("Great! You're as smart as me.")
                        break
                    else:
                        choice = "player"
