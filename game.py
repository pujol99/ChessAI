import pygame
import chess
import utils
from board import Board
from AI import AI

INFINITY = 9999
WIDTH = 400
HEIGHT = 400


def game_loop(screen, white_turn):
    board = Board(screen)
    ai_engine = AI()
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
                    i, j = utils.chess_index(x, y)
                    if board.is_white((i, j)) and white_turn:
                        start = i, j
                    elif start and board.make_move(start, (i, j)):
                        game_over = board.board.is_game_over()
                        start = None
                        white_turn = not white_turn
        else:
            move = ai_engine.minimax(5, board, white_turn, -INFINITY, INFINITY)
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
