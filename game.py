import pygame
import chess
from math import inf as infinity
from image import Image
from board import Board


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

def render_selections(screen, image, start):
    if start:
        i, j = start
        j = 7 - j
        screen.blit(image.start, (i*50, j*50))

def game_over(white_turn):
    if white_turn:
        print('white wins')
    else:
        print('black wins')

def minimax(depth, board, white_turn, alpha, beta):
    if white_turn:
        best = [None, +infinity]
    else:
        best = [None, -infinity]

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
    image = Image()
    _quit = False
    start = None
    game_over = False
    #LOOP
    while not game_over and not _quit:
        #PROCESS EVENTS
        if white_turn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    _quit = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    i, j = chess_index(x, y)
                    xC, yC = chess_index(x, y)
                    if board.is_white((i, j)) and white_turn:
                        start = i, j
                    elif start and board.make_move(start, (i, j)):
                        game_over = board.board.is_game_over()
                        if game_over:
                            game_over(white_turn)
                        start = None
                        white_turn = not white_turn
        else:
            move = minimax(5, board, white_turn, -infinity, infinity)
            board.board.push(move[0])
            white_turn = not white_turn
        #UPDATE VALUES AND CONDITIONS

        #DRAW
        screen.fill(image.bg)
        board.render_board()
        render_selections(screen, image, start)
        board.render_pieces()
        pygame.display.flip()

def main():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess')
	
    game_loop(screen, True)	

if __name__ == '__main__':
    main()
