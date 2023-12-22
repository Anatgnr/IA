from termcolor import colored
import Heuristique
import Reversi

def select_heuristic():
    board = Reversi.Board(10)
    while True:
        print("-------------------------------")
        print(colored("1: Mobilité et Coins", "green"))
        print(colored("2: Nombre de pièces, Mobilité, Coins et Stabilité", "green"))
        print(colored("3: Mobilité", "green"))
        print(colored("4: Nombre de pièces", "magenta"))
        print(colored("5: Position", "yellow"))
        print(colored("6: Mobilité", "white"))
        print(colored("7: Position stratégique", "white"))
        print(colored("8: Coins", "green"))
        print(colored("9: Stabilité", "green"))
        print(colored("10: Nombre de pièces et Mobilité", "white"))
        print(colored("q: Quitter", "red"))
        user_input = input("Choisissez l'heuristique a utiliser: ")
        print("-------------------------------")
        if user_input == "1":
            # print(Heuristique.hMobAndCo)
            return Heuristique.hMobAndCo
        elif user_input == "2":
            return Heuristique.fullHeuristique
        elif user_input == "3":
            return Heuristique.hMobility
        elif user_input == "4":
            return Heuristique.hNbPieces
        elif user_input == "5":
            return Heuristique.hPos
        elif user_input == "6":
            return Heuristique.hMobility
        elif user_input == "7":
            return Heuristique.hPos
        elif user_input == "8":
            return Heuristique.hCorners
        elif user_input == "9":
            return Heuristique.hStability
        elif user_input == "10":
            return Heuristique.hNbAndMob
        elif user_input == "q":
            exit()
        else:
            print('')
            print("##############")
            print(colored("Choix invalide", "red"))
            print("##############")
            print('')
            select_heuristic()
