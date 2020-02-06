from pieces import *
import pygame
import copy

SELECTED_START = pygame.image.load(os.path.abspath('imgs/selected_orign.png'))
OBJECTIVE = pygame.image.load(os.path.abspath('imgs/objective.png'))
ATTACK = pygame.image.load(os.path.abspath('imgs/attack.png'))

class Board:
    def __init__(self):
        self.spots = self.reset_board()
        self.whites = []
        self.get_whites()
        self.blacks = []
        self.get_blacks()
    
    def get_position(self, position):
        x, y = position
        return self.spots[y][x]
    
    def get_whites(self):
        for row in self.spots:
            for spot in row:
                if spot.piece.is_white == True:
                    self.whites.append(spot)

    def get_blacks(self):
        for row in self.spots:
            for spot in row:
                if spot.piece.is_white == False:
                    self.blacks.append(spot)

    def compute_moves(self, whites):
        if whites:
            for white in self.whites:
                white.piece.positions_can_move(self.spots, white)
        else:
            for black in self.blacks:
                black.piece.positions_can_move(self.spots, black)

    def get_copy(self):
        return copy.copy(self.spots)

    def print_pieces(self):
        for white in self.whites:
                print(white.piece.name)
        for black in self.blacks:
                print(black.piece.name)

    def get_moves(self, whites):
        moves = []
        if whites:
            for white in self.whites:
                for move in white.piece.positions:
                    moves.append(move)
        else:
            for black in self.blacks:
                for move in black.piece.positions:
                    moves.append(move)
        return moves
                
    def draw_pieces(self, screen):
        for row in self.spots:
            for spot in row:
                spot.draw_piece(screen)
    
    def select_objectives(self, position):
        for spot in position.piece.positions:
            spot[1].selected_end = True

    def unselect_pieces(self):
        for row in self.spots:
            for spot in row:
                spot.selected_start = False
                spot.selected_end = False
            

    def make_move(self, move):
        start, end = move[0], move[1]   

        end.piece = copy.copy(start.piece)
        end.piece.has_moved = True
        start.piece = Blank()

        self.get_blacks()
        self.get_whites()
    
    def print_board(self):
        for row in self.spots:
            for spot in row:
                print(spot.piece.name, end=' ')
            print('')
        print('-------------------------------')

    def reset_board(self):
        spots = [
            [Spot(0, 0, Rook(False)), Spot(1, 0, Knight(False)), Spot(2, 0, Bishop(False)), Spot(3, 0, Queen(False)), 
            Spot(4, 0, King(False)), Spot(5, 0, Bishop(False)), Spot(6, 0, Knight(False)), Spot(7, 0, Rook(False))],
            [Spot(0, 1, Pawn(False)), Spot(1, 1, Pawn(False)), Spot(2, 1, Pawn(False)), Spot(3, 1, Pawn(False)), 
            Spot(4, 1, Pawn(False)), Spot(5, 1, Pawn(False)), Spot(6, 1, Pawn(False)), Spot(7, 1, Pawn(False))],
            [Spot(0, 2, Blank()), Spot(1, 2, Blank()), Spot(2, 2, Blank()), Spot(3, 2, Blank()),
            Spot(4, 2, Blank()), Spot(5, 2, Blank()), Spot(6, 2, Blank()), Spot(7, 2, Blank())],
            [Spot(0, 3, Blank()), Spot(1, 3, Blank()), Spot(2, 3, Blank()), Spot(3, 3, Blank()),
            Spot(4, 3, Blank()), Spot(5, 3, Blank()), Spot(6, 3, Blank()), Spot(7, 3, Blank())],
            [Spot(0, 4, Blank()), Spot(1, 4, Blank()), Spot(2, 4, Blank()), Spot(3, 4, Blank()),
            Spot(4, 4, Blank()), Spot(5, 4, Blank()), Spot(6, 4, Blank()), Spot(7, 4, Blank())],
            [Spot(0, 5, Blank()), Spot(1, 5, Blank()), Spot(2, 5, Blank()), Spot(3, 5, Blank()),
            Spot(4, 5, Blank()), Spot(5, 5, Blank()), Spot(6, 5, Blank()), Spot(7, 5, Blank())],
            [Spot(0, 6, Pawn(True)), Spot(1, 6, Pawn(True)), Spot(2, 6, Pawn(True)), Spot(3, 6, Pawn(True)), 
            Spot(4, 6, Pawn(True)), Spot(5, 6, Pawn(True)), Spot(6, 6, Pawn(True)), Spot(7, 6, Pawn(True))],
            [Spot(0, 7, Rook(True)), Spot(1, 7, Knight(True)), Spot(2, 7, Bishop(True)), Spot(3, 7, Queen(True)), 
            Spot(4, 7, King(True)), Spot(5, 7, Bishop(True)), Spot(6, 7, Knight(True)), Spot(7, 7, Rook(True))]
        ]
        return spots


class Spot:
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.piece = piece
        self.selected_start = False
        self.selected_end = False
        self.dragging = False
        self.imgX = self.x * 50
        self.imgY = self.y * 50

    def reset_drag(self):
        self.dragging = False
        self.imgX = self.x * 50
        self.imgY = self.y * 50
    
    def get_pos(self):
        return self.x, self.y

    def draw_piece(self, screen):
        if self.selected_start:
            screen.blit(SELECTED_START, (self.x * 50, self.y * 50))
        if self.piece.threatened:
            screen.blit(ATTACK, (self.x * 50, self.y * 50))
        if self.selected_end:
            screen.blit(OBJECTIVE, (self.x * 50, self.y * 50))
        if self.piece.is_white != None:
            img = self.piece.get_img()
            if img:
                if self.dragging:
                    screen.blit(img, (self.imgX, self.imgY))
                else:
                    screen.blit(img, (self.x * 50, self.y * 50))
