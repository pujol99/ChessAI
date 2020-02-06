import pygame
import os
import copy
import time
from random import choice
from board import Board, Spot
from pieces import *
import pieces

#CONSTANTS
WIDTH = 400
HEIGHT = 400
FONT = 'freesansbold.ttf'

#IMAGES
BOARD = pygame.image.load(os.path.abspath('imgs/board.png'))

#COLORS
BLUE = pygame.Color('0x4363d8')
DARK_BLUE = pygame.Color('0x000075')
SOFT_BLUE = pygame.Color('0x46f0f0')
BACK = pygame.Color('0xf58231')
WHITE = pygame.Color('0xffffff')
BLACK = pygame.Color('0x000000')

def get_index_click():
    x, y = pygame.mouse.get_pos()
    i = x//50
    j = y//50
    return i, j

def text(screen, size, text, bg, fg, cx, cy):
	font = pygame.font.Font(FONT, size) 
	text = font.render(text, True, fg, bg) 
	textRect = text.get_rect()  
	textRect.center = (cx, cy)
	screen.blit(text, textRect)

def select_start(board, i, j, white_turn):
    if board.spots[j][i].piece.is_white == white_turn:
        start = board.spots[j][i]
        start.dragging = True
        start.selected_start = True
        board.select_objectives(start)
        return start
    return None


def game_loop(screen, white_turn):
    board = Board()
    aux_board = Board()
    #LOCAL VARIABLES
    running = True
    start = None
    end = None
    #COMPUTE POSIBLE MOVES
    board.compute_moves(white_turn)
    current_moves = board.get_moves(white_turn)
    #LOOP
    while running:
        #PROCESS EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    i, j = get_index_click()
                    start = select_start(board, i, j, white_turn)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start:
                    i, j = get_index_click()
                    end = board.spots[j][i]
                    start.reset_drag()
                    if end.selected_end:
                        board.make_move((start, end))
                        white_turn = not white_turn
                        board.compute_moves(white_turn)
                        current_moves = board.get_moves(white_turn)
                        prev_moves = board.get_moves(not white_turn)
                    start = None
                    board.unselect_pieces()

            elif event.type == pygame.MOUSEMOTION:
                if start:
                    xC, yC = pygame.mouse.get_pos()
                    start.imgX = xC - 25
                    start.imgY = yC - 25
      
        #UPDATE VALUES AND CONDITIONS

        #DRAW
        screen.fill(BLACK)
        screen.blit(BOARD,(0, 0))
        
        board.draw_pieces(screen)
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess')
	
    game_loop(screen, True)	

if __name__ == '__main__':
    main()
