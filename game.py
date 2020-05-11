import pygame
import chess
from board import Board

INFINITY = 9999
WIDTH = 400
HEIGHT = 400

def chess_index(x, y):
    i = x//50
    j = 7 - y//50
    return i, j

def click_index(x, y):
    i = x//50
    j = y//50
    return i, j

def game_over(white_turn):
    if white_turn:
        print('white wins')
    else:
        print('black wins')

def minimax(depth, board, white_turn, alpha, beta):
    if white_turn:
        best = [None, +INFINITY]
    else:
        best = [None, -INFINITY]

    if not depth:
        score = board.evaluate_board()
        return [None, score]
    
    moves = board.board.legal_moves
    for move in moves:
        board.board.push(move)
        value = minimax(depth-1, board, not white_turn, alpha, beta)
        board.board.pop()

        if white_turn:
            if value[1] < best[1]:
                value[0] = move
                best = value
            beta = min(beta, value[1])
            if beta <= alpha:
               break
        if not white_turn:
            if value[1] > best[1]:
                value[0] = move
                best = value
            alpha = max(alpha, value[1])
            if beta <= alpha:
                break
    return best


def game_loop(screen, white_turn):
    board = Board(screen)
    start = None
    game_over = False

    has_quit = False
    #LOOP
    while not game_over and not has_quit:
        #PROCESS EVENTS
        if white_turn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    has_quit = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    i, j = chess_index(x, y)
                    xC, yC = chess_index(x, y)
                    if board.is_white((i, j)) and white_turn:
                        start = i, j
                    elif start and board.make_move(start, (i, j)):
                        game_over = board.board.is_game_over()
                        start = None
                        white_turn = not white_turn
        else:
            move = minimax(5, board, white_turn, -INFINITY, INFINITY)
            board.board.push(move[0])
            white_turn = not white_turn

        

        #DRAW
        board.render_board()
        board.render_selections(start)
        board.render_pieces()
        pygame.display.flip()

def main():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess')
	
    game_loop(screen, True)	

if __name__ == '__main__':
    main()
