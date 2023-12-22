import Reversi
import Min_max
import Select_Heuristique as Slct
from termcolor import colored

def play_game(player1, player2):
    board = Reversi.Board(10)
    cpt = 0
    while not board.is_game_over():
        # print(board)
        # MinMax joue les NOIRS
        if board._nextPlayer == board._BLACK:
            move = player1(board)
            board.push(move)
            cpt += 1
        # random_move joue les BLANCS
        else:
            move = player2(board)
            board.push(move)
            cpt += 1
    rslt = board._nbBLACK - board._nbWHITE
    if rslt > 0:
        print(colored(f"L'IA1 a gagné", "red"))
        print(board)
    elif rslt < 0:
        print(colored(f"L'IA2 a gagné", "blue"))
        print(board)
    return rslt

def main():
    heuristic1 = Slct.select_heuristic()
    heuristic2 = Slct.select_heuristic()
    play_game(lambda board: Min_max.minmax3(board, 2, heuristic1)[1], lambda board: Min_max.minmax3(board, 2, heuristic2)[1])
    return 