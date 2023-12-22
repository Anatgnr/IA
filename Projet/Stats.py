import time
import Min_max
import IA_vs_RandMove as IVR
import Select_Heuristique as Slct
import Select_depth as Sld
from termcolor import colored

def games(nb_games, depth, heuristic):
    sum = 0
    start = time.time()
    match_result = []
    # print("running")
    for i in range(nb_games):
        #Si les NOIRS gagnent, on ajoute 1 à la somme
        print(f"running game n°{i}")
        # print(colored(heuristic, "red"))
        start2 = time.time()
        play = IVR.play_game(lambda board:Min_max.minmax3(board, depth, heuristic, maximizingPlayer=True)[1] , IVR.random_move)
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

def main():
    nb_games = input("renseignez le nombre de parties à jouer:")
    if not(nb_games.isdigit()):
        print(f"Vous devez entré un entier")
        main()
    depth = Sld.select_depth()
    heuristic = Slct.select_heuristic()
    # print(heuristic(board = Reversi.Board(10)))
    print(heuristic)
    games(int(nb_games), depth, heuristic)
    return