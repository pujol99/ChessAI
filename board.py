import chess
import random
import pygame
from image import Image


class Board:
    def __init__(self, screen):
        self.board = chess.Board()
        self.chess = chess
        self.screen = screen
        self.image = Image()

        self.piece_dict = {
            'r': self.image.bTower,
            'n': self.image.bHorse,
            'b': self.image.bBishop,
            'q': self.image.bQueen,
            'k': self.image.bKing,
            'p': self.image.bPawn,
            'R': self.image.wTower,
            'N': self.image.wHorse,
            'B': self.image.wBishop,
            'Q': self.image.wQueen,
            'K': self.image.wKing,
            'P': self.image.wPawn
        }

        self.piece_values = {
            'r': 50,
            'n': 30,
            'b': 30,
            'q': 90,
            'k': 900,
            'p': 10,
            'R': 50,
            'N': 30,
            'B': 30,
            'Q': 90,
            'K': 900,
            'P': 10
        }

    def get_square_name(self, number):
        return self.chess.square_name(number)
    
    def get_piece(self, number):
        return self.board.piece_at(number)

    def index(self, pos):
        i, j = pos
        return i + 8*j

    def make_move(self, start, end):
        try:
            move = self.board.find_move(self.index(start), self.index(end))
        except:
            return False
        self.board.push(move)
        return True
        
    def evaluate_board(self):
        value = 0
        for i in range(0, 63):
            try:
                x = bool(self.board.piece_at(i).color)
            except:
                continue
            if x:
                value -= self.piece_values[str(self.board.piece_at(i))]
            else:
                value += self.piece_values[str(self.board.piece_at(i))]
        return value



    def is_white(self, pos):
        x, y = pos[0], pos[1]
        piece = self.board.piece_at(x + 8*y)
        if piece:
            return piece.color
        return False
    
    def is_black(self, pos):
        x, y = pos[0], pos[1]
        piece = self.board.piece_at(x + 8*y)
        if piece:
            return not piece.color
        return False

    def render_pieces(self):
        pieces_str = self.board.fen().split(' ')[0]
        x, y = 0, 0
        for char in pieces_str:
            if '/' in char:
                y += 1
                x = 0
            elif char.isnumeric():
                x += int(char)
            else:
                self.screen.blit(self.piece_dict[char], (x*50,y*50))
                x += 1
    
    def render_board(self):
        self.screen.blit(self.image.board,(0, 0))
