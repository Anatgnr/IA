import time
import Min_max
import Reversi
import Select_Heuristique as Slct
import IA_vs_RandMove as IVR
from termcolor import colored

def iterative_deepening(board, heuristique, max_time_seconds):
    start_time = time.time()
    max_depth = 1

    while time.time() - start_time < max_time_seconds:
        best_move = Min_max.minmax3(board, max_depth, heuristique)[1]
        max_depth += 1

    return best_move

def main():
    heuristique = Slct.select_heuristic()
    input_time = input("Entrez le temps de recherche en secondes: ")
    if not(input_time.isdigit()):
        print(f"Vous devez entré un entier")
        main()
    else :
        max_time_seconds = int(input_time)
    print(colored("running", "green"))
    start = time.time()
    IVR.play_game(lambda board: iterative_deepening(board, heuristique, max_time_seconds), IVR.random_move)
    end = time.time()
    execution_time = end - start
    print(colored(f"Execution time: {execution_time}", "green"))
    return
