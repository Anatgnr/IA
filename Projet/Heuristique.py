# File n°2
import Reversi

# Dans ce fichier, on s'occupe de trouver une heuristique
# cohérante pour le jeu de Reversi

# NB PIECES
def hNbPieces(board):
    # On compte le nombre de pieces de chaque joueur
    player = board._WHITE
    player_pieces = sum([row.count(player) for row in board._board])
    opponent_pieces = sum([row.count(board._flip(player)) for row in board._board])
    total = player_pieces + opponent_pieces
    if total == 0:
        return 0
    return 100 * (player_pieces - opponent_pieces) / total

# MOBILITE
def hMobility(board):
    player = board._WHITE
    # On compare la mobilité de chaque joueur, la marge de manoeuvre
    player_mobility = len(board.legal_moves())
    opponent_mobility = len(board.legal_moves())
    # evaluation = player_pieces - opponent_pieces + (player_mobility - opponent_mobility)
    total = player_mobility + opponent_mobility
    if total == 0:
        return 0
    return 100 * (player_mobility - opponent_mobility / total)

# Position strategique des pieces
# Heuristique couteuse en temps de calcul
def hPos(board):
    # On défini un tableau de poids
    player = board._WHITE
    weights = [
    [4, -3, 2, 2, 2, 2, 2, -3, 4, 4],
    [-3, -4, -1, -1, -1, -1, -1, -4, -3, -3],
    [2, -1, 1, 0, 0, 0, 1, -1, 2, 2],
    [2, -1, 0, 1, 0, 0, 1, 0, 2, 2],
    [2, -1, 0, 0, 1, 1, 0, -1, 2, 2],
    [2, -1, 0, 0, 1, 1, 0, -1, 2, 2],
    [2, -1, 1, 1, 0, 0, 1, -1, 2, 2],
    [-3, -4, -1, -1, -1, -1, -1, -4, -3, -3],
    [4, -3, 2, 2, 2, 2, 2, -3, 4, 4],
    [4, -3, 2, 2, 2, 2, 2, -3, 4, 4]
]
    score = 0
    for i in range(board.get_board_size()):
        for j in range(board.get_board_size()):
            piece = board._board[i][j]
            if piece == board._WHITE:
                score += weights[i][j]
            elif piece == board._BLACK:
                score -= weights[i][j]
    return score

# COINS
def hCorners(board):
    player = board._WHITE
    scoreW = 0
    scoreB = 0
    if board._board[0][0] == player:
        scoreW += 1
    if board._board[0][0] == board._flip(player):
        scoreB += 1
    if board._board[0][9] == player:
        scoreW += 1
    if board._board[0][9] == board._flip(player):
        scoreB += 1
    if board._board[9][0] == player:
        scoreW += 1
    if board._board[9][0] == board._flip(player):
        scoreB += 1
    if board._board[9][9] == player:
        scoreW += 1
    if board._board[9][9] == board._flip(player):
        scoreB += 1
    if scoreB + scoreW == 0:
        return 0
    return 100 * ((scoreB - scoreW) / (scoreB + scoreW))

def hStability(board):
        max_player_stability, min_player_stability = calculate_stability(board)

        stability_weights = {
            'stable': 1,
            'semi-stable': 0.5,
            'unstable': 0
        }

        max_player_value = sum([stability_weights[category] * count for category, count in max_player_stability.items()])
        min_player_value = sum([stability_weights[category] * count for category, count in min_player_stability.items()])

        total_value = max_player_value + min_player_value

        if total_value == 0:
            return 0
        return  100 * (max_player_value - min_player_value) / total_value


def calculate_stability(board):
    max_player_stability = {'stable': 0, 'semi-stable': 0, 'unstable': 0}
    min_player_stability = {'stable': 0, 'semi-stable': 0, 'unstable': 0}

    for x in range(board._boardsize):
        for y in range(board._boardsize):
            if board._board[x][y] == board._WHITE:
                category = get_stability_category(board, x, y, board._WHITE)
                max_player_stability[category] += 1
            elif board._board[x][y] == board._BLACK:
                category = get_stability_category(board, x, y, board._BLACK)
                min_player_stability[category] += 1

    return max_player_stability, min_player_stability


def get_stability_category(board, x, y, player):
    # Détermine la catégorie de stabilité d'une pièce
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for neighbor in neighbors:
        nx, ny = neighbor
        if 0 <= nx < board._boardsize and 0 <= ny < board._boardsize:
            if board._board[nx][ny] == player:
                return 'stable'
            elif board._board[nx][ny] == board._EMPTY:
                return 'semi-stable'

    return 'unstable'

# NBPPIECES + MOBILITE
# Au final, l'heuristique est la somme des pieces et de la mobilité
# On constate de meilleurs résultats sans le nombre de pieces
def hNbAndMob(board):
    return hNbPieces(board) + hMobility(board)

# très très chaud ça -> best one 
# 92%
def hMobAndCo(board):
    return 20 * hMobility(board) + 80* hCorners(board)

# NBPIECES + MOBILITE + Pos strat
# priorité sur les pos strat et la mobilité
# 84%
def fullHeuristique(board):
    return 25 * hNbPieces(board) + 5 * hMobility(board) + 30 * hCorners(board) + 25 * hStability(board)