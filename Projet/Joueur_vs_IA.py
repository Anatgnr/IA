import Reversi
import Min_max
import Select_Heuristique as Slct
from termcolor import colored

def human_play(board):
    try:
        print("Entrez les coordonnées de votre coup (format : x y) : ")
        move = input().split()
        x, y = map(int, move)
        return [board._WHITE, x, y]
    except (ValueError, IndexError):
        print("Format de mouvement incorrect. Réessayez.")
        return human_play(board)
    
def HumanVsAI(board, depth, heuristic):
    while not board.is_game_over():
        legal_moves = list(board.legal_moves())
        print(board)
        if board._nextPlayer == board._BLACK:
            _, move = Min_max.minmax3(board, depth, heuristic)
            board.push(move)
        elif board._nextPlayer == board._WHITE:
            for my_list in legal_moves:
                # Utilisation de la notation de découpage pour imprimer [2, 3]
                print(my_list[1:])
            #print(legal_moves[1:])
            move = human_play(board)
            board.push(move)
        else:
            print("Erreur")
    print(board)
    rslt = board._nbBLACK - board._nbWHITE
    if board.is_tie():
        print("Match nul")
    elif rslt > 0:
        print(colored("L'IA a gagné", "red"))
    else:
        print(colored("Vous avez gagné", "blue"))


def main():
    board = Reversi.Board(10)
    heuristic = Slct.select_heuristic()
    print(f"vous jouez les BLANCS, l'IA joue les NOIRS")
    HumanVsAI(board, 2, heuristic)
    return 