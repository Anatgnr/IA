import random
from termcolor import colored

def select_depth():
    print("-------------------------------")
    print(colored("nombre entier:", "green"))
    print(colored("r: Nombre aléatoir entre 1 et 6", "blue"))
    print(colored("q: Quitter", "red"))
    user_input = input(colored("choisissez la profondeur de l'IA: ", "green"))
    print("-------------------------------")
    if not(user_input.isdigit() or 'r' or 'q'):
        print("##############")
        print(colored("Vous devez entré un entier ou r ou q","red"))
        print("##############")
        select_depth()
    elif user_input == "r":
        rv = random.randint(1, 6)
        print ("profondeur choisie : ", rv)
        return rv
    elif user_input == "q":
        exit()
    else :
        return int(user_input)
