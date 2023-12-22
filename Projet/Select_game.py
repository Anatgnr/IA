import IA_vs_RandMove
import Joueur_vs_IA
import IA_vs_IA
import Stats
import Iterative_deepening
from termcolor import colored

def select_game():
    print("-------------------------------")
    print(colored("1: IA vs Random moves", "magenta"))
    print(colored("2: Joueur vs IA", "green"))
    print(colored("3: IA vs IA", "yellow"))
    print(colored("4: Statistiques IA vs Random moves", "blue"))
    print(colored("5: Iterative deepening", "cyan"))
    print(colored("q: Quitter", "red"))
    user_input = input("Choisissez le mode de jeu: ")
    print("-------------------------------")
    if user_input == "1":
        IA_vs_RandMove.main()
    elif user_input == "2":
        Joueur_vs_IA.main()
    elif user_input == "3":
        IA_vs_IA.main()
    elif user_input == "4":
        Stats.main()
    elif user_input == "5":
        Iterative_deepening.main()
    elif user_input == "q":
        exit()
    else:
        print('')
        print("##############")
        print(colored("Choix invalide", "red"))
        print("##############")
        print('')
        select_game()

select_game()