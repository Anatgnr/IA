# File n°1
import Reversi
import time

# Dans ce fichier, on s'occupe de coder un brute force non optimisé

def explore_all_games(board, depth):
    result = {"total_games":0, "noeuds":0}
    start = time.time()
    def explore(board, depth):
        if depth == 0:
            result["noeuds"] += 1
            return
        if board.is_game_over():
            result["total_games"] += 1
            return
        else:
            for move in board.legal_moves():
                result["noeuds"] += 1
                board.push(move)
                explore(board, depth - 1)
                board.pop()
    explore(board, depth)
    result["noeuds"] -= 1
    end = time.time()
    execution_time = end - start
    print("Execution time: ", execution_time)
    print (result)

board = Reversi.Board(10)
print(f"resultat pour depth = 5 : {explore_all_games(board, 5)}")

#Pour une profondeur de 10 on a 232 games, 53818347 noeuds et un temps d'execution de 1306.6 secondes



