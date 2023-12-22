# File n°3
import Reversi
import Heuristique
from random import choice

# Dans ce fichier, on s'occupe de coder l'algorithme MinMax
# avec l'heuristique qu'on a trouvé dans heuristique.py

def min_value(board, depth, alpha, beta):
    if depth == 0 or board.is_game_over():
        return Heuristique.hMobAndCo(board)
        # return board.heuristique()

    min_eval = float('inf')
    for move in board.legal_moves():
        board.push(move)
        eval = max_value(board, depth - 1, alpha, beta)
        board.pop()
        min_eval = min(min_eval, eval)
        beta = min(beta, min_eval)
        if beta <= alpha:
            break  # Élagage alpha-bêta
    return min_eval

def max_value(board, depth, alpha, beta):
    if depth == 0 or board.is_game_over():
        return Heuristique.hMobAndCo(board)
        # return board.heuristique()

    max_eval = float('-inf')
    for move in board.legal_moves():
        board.push(move)
        eval = min_value(board, depth - 1, alpha, beta)
        board.pop()
        max_eval = max(max_eval, eval)
        alpha = max(alpha, max_eval)
        if beta <= alpha:
            break  # Élagage alpha-bêta
    return max_eval

# MinMax sans elagage
def minmaxEF(board, depth):
    if depth == 1:
        best_moves = []
        max_eval = float('-inf')
        for move in board.legal_moves():
            board.push(move)
            eval = min_value(board, depth - 1, float('-inf'), float('inf'))
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_moves = [move]
            elif eval == max_eval:
                best_moves.append(move)
        return max_eval, choice(best_moves)
    else:
        max_eval = float('-inf')
        best_move = None
        for move in board.legal_moves():
            board.push(move)
            eval = min_value(board, depth - 1, float('-inf'), float('inf'))
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move

        return max_eval, best_move


def minmax(board, depth, maximizingPlayer=True, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or board.is_game_over():
        return Heuristique.hMobAndCo(board), None
        # return board.heuristique(), None

    legal_moves = board.legal_moves()  # Appel de la méthode
    best_move = legal_moves[0]  # Initialisation avec le premier mouvement
    if maximizingPlayer:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minmax(board, depth - 1, False, alpha, beta)[0]
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Élagage alpha-bêta
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minmax(board, depth - 1, True, alpha, beta)[0]
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Élagage alpha-bêta
        return min_eval, best_move
    
# meme fonction que minmax mais permet de spécifier une heuristique différente de celle de minmax
def minmax2(board, depth, maximizingPlayer=True, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or board.is_game_over():
        print("heuristique", Heuristique.hMobility(board))
        return Heuristique.hMobility(board), None
        # return board.heuristique(), None

    legal_moves = board.legal_moves()  # Appel de la méthode
    best_move = legal_moves[0]  # Initialisation avec le premier mouvement
    if maximizingPlayer:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minmax2(board, depth - 1, False, alpha, beta)[0]
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Élagage alpha-bêta
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minmax2(board, depth - 1, True, alpha, beta)[0]
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Élagage alpha-bêta
        return min_eval, best_move
    
# Permet de passer l'heuristique en parametre
def minmax3(board, depth, heuristique, maximizingPlayer=True, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or board.is_game_over():
        return heuristique(board), None
        # return board.heuristique(), None

    legal_moves = board.legal_moves()  # Appel de la méthode
    best_move = legal_moves[0]  # Initialisation avec le premier mouvement
    if maximizingPlayer:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minmax3(board, depth - 1,  heuristique, False, alpha, beta)[0]
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Élagage alpha-bêta
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minmax3(board, depth - 1, heuristique, True, alpha, beta)[0]
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Élagage alpha-bêta
        return min_eval, best_move
    

# board = Reversi.Board(10)
# result = minmax(board, 5, True)
# score, best_move = minmax(board, 5)
# print(f"Score: {score}, Best Move: {best_move}")