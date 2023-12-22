# File n°4
import Reversi
import Min_max
import random
import time
import Heuristique
import Select_Heuristique as Slct
from termcolor import colored

# Dans ce fichier, on s'occupe de coder un simulateur de jeu
# Les Noirs commencent toujours
def random_move(board):
    moves = list(board.legal_moves())
    return random.choice(moves)

def play_game(player1, player2):
    board = Reversi.Board(10)
    cpt = 0
    while not board.is_game_over():
        # print(board)
        # player1
        # MinMax joue les NOIRS
        if board._nextPlayer == board._BLACK:
            move = player1(board)
            board.push(move)
            cpt += 1
        #player2
        # random_move joue les BLANCS
        else:
            move = player2(board)
            board.push(move)
            cpt += 1
    rslt = board._nbBLACK - board._nbWHITE
    if rslt > 0:
        print(colored(f"L'IA a gagné", "red"))
        print(board)
    elif rslt < 0:
        print(colored(f"RandomMove a gagné", "blue"))
        print(board)
    return rslt

# def main():
#     heuristic = Slct.select_heuristic()
#     play_game(lambda board: Min_max.minmax3(board, 2, heuristic(board))[1], random_move)
#     return 

def games(nb_games, depth):
    sum = 0
    start = time.time()
    match_result = []
    # print("running")
    for i in range(nb_games):
        #Si les NOIRS gagnent, on ajoute 1 à la somme
        print(f"running game n°{i}")
        start2 = time.time()
        play = play_game(lambda board:Min_max.minmax2(board, depth)[1] , random_move)
        # play = play_game(lambda board: Min_max.minmax(board, 2)[1], lambda board: Min_max.minmax2(board, 2)[1])
        if  play > 0:
            sum += 1
            match_result += (colored("B", "red"))
            print(colored("B", "red"))
        elif play < 0:
            match_result += (colored("W", "blue"))
            print(colored("W", "blue"))
        else:
            match_result += (colored("D", "green"))
            print(colored("D", "green"))
        end2 = time.time()
        print(f"temps d'execution = {end2-start2}")
    end = time.time()
    execution_time = end - start
    print("Execution time: ", execution_time)
    print(f"Pour {int(nb_games)} parties, la moyenne de victoire pour l'ia est de {((sum)/int(nb_games))*100}%")
    print(f"Le nombre de victoire est de {sum} pour {int(nb_games)} parties")
    print("".join(match_result))

# games(10, 4, Heuristique.hNbPieces)