import pygame, os

BLACK_ROOK = pygame.image.load(os.path.abspath('imgs/blackTower.png'))
BLACK_KNIGHT = pygame.image.load(os.path.abspath('imgs/blackHorse.png'))
BLACK_BISHOP = pygame.image.load(os.path.abspath('imgs/blackBishop.png'))
BLACK_KING = pygame.image.load(os.path.abspath('imgs/blackKing.png'))
BLACK_QUEEN = pygame.image.load(os.path.abspath('imgs/blackQueen.png'))
BLACK_PAWN = pygame.image.load(os.path.abspath('imgs/blackPawn.png'))
WHITE_ROOK = pygame.image.load(os.path.abspath('imgs/whiteTower.png'))
WHITE_KNIGHT = pygame.image.load(os.path.abspath('imgs/whiteHorse.png'))
WHITE_BISHOP = pygame.image.load(os.path.abspath('imgs/whiteBishop.png'))
WHITE_KING = pygame.image.load(os.path.abspath('imgs/whiteKing.png'))
WHITE_QUEEN = pygame.image.load(os.path.abspath('imgs/whiteQueen.png'))
WHITE_PAWN = pygame.image.load(os.path.abspath('imgs/whitePawn.png'))

class Piece:
    def __init__(self, white=None):
        self.positions = []
        self.is_white = white
        self.has_moved = False
        self.threatened = False 
        self.name = None
        self.test = False
    
    def positions_can_move(self, spots, start):
        pass
    
    def get_img(self):
        pass

    def color(self):
        if self.is_white:
            self.name = "w"
        else:
            self.name = "b"

    def while_loop(self, spots, start, x, y, x_inc, y_inc):
        while self.inside_board(x, y):
            if spots[y][x].piece.is_white == self.is_white:
                break
            elif spots[y][x].piece.is_white == (not self.is_white):
                self.positions.append((start, spots[y][x]))
                break
            else:
                self.positions.append((start, spots[y][x]))
            x += x_inc
            y += y_inc

    def inside_board(self, x, y):
        if x > 7 or x < 0 or y > 7 or y < 0:
            return False
        return True
        

class Blank(Piece):
    def __init__(self, white=None):
        super().__init__(white=white)
        self.name = "blank"

    def get_img(self):
        return

class Rook(Piece):
    def __init__(self, white=None):
        super().__init__(white=white)
        self.color()
        self.name += "rook"

    def positions_can_move(self, spots, start):
        self.positions.clear()
        x, y = start.x + 1, start.y
        self.while_loop(spots, start, x, y, 1, 0)
        x, y = start.x - 1, start.y
        self.while_loop(spots, start, x, y,-1, 0)
        x, y = start.x, start.y + 1
        self.while_loop(spots, start, x, y, 0, 1)
        x, y = start.x, start.y - 1
        self.while_loop(spots, start, x, y, 0,-1)
    
    def get_img(self):
        if self.is_white:
            return WHITE_ROOK
        return BLACK_ROOK

class Knight(Piece):
    def __init__(self, white=None):
        super().__init__(white=white)
        self.color()
        self.name += "knight"

    def positions_can_move(self, spots, start):
        self.positions.clear()
        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i) + abs(j) == 3:
                    if self.inside_board(start.x + i, start.y + j):
                        x, y = start.x + i, start.y + j
                        if spots[y][x].piece.is_white != self.is_white:
                            self.positions.append((start, spots[y][x]))

    def get_img(self):
        if self.is_white:
            return WHITE_KNIGHT
        return BLACK_KNIGHT
        

class Bishop(Piece):
    def __init__(self, white=None):
        super().__init__(white=white)
        self.color()
        self.name += "bishop"

    def positions_can_move(self, spots, start):
        self.positions.clear()
        x, y = start.x + 1, start.y + 1
        self.while_loop(spots, start, x, y, 1, 1)
        x, y = start.x - 1, start.y - 1
        self.while_loop(spots, start, x, y,-1,-1)
        x, y = start.x - 1, start.y + 1
        self.while_loop(spots, start, x, y,-1, 1)
        x, y = start.x + 1, start.y - 1
        self.while_loop(spots, start, x, y, 1,-1)
    
    def get_img(self):
        if self.is_white:
            return WHITE_BISHOP
        return BLACK_BISHOP

class Queen(Piece):
    def __init__(self, white=None):
        super().__init__(white=white)
        self.color()
        self.name += "queen"

    def positions_can_move(self, spots, start):
        self.positions.clear()
        x, y = start.x + 1, start.y
        self.while_loop(spots, start, x, y, 1, 0)
        x, y = start.x - 1, start.y
        self.while_loop(spots, start, x, y,-1, 0)
        x, y = start.x, start.y + 1
        self.while_loop(spots, start, x, y, 0, 1)
        x, y = start.x, start.y - 1
        self.while_loop(spots, start, x, y, 0,-1)
        x, y = start.x + 1, start.y + 1
        self.while_loop(spots, start, x, y, 1, 1)
        x, y = start.x - 1, start.y - 1
        self.while_loop(spots, start, x, y,-1,-1)
        x, y = start.x - 1, start.y + 1
        self.while_loop(spots, start, x, y,-1, 1)
        x, y = start.x + 1, start.y - 1
        self.while_loop(spots, start, x, y, 1,-1)
    
    def get_img(self):
        if self.is_white:
            return WHITE_QUEEN
        return BLACK_QUEEN

class King(Piece):
    def __init__(self, white=None):
        super().__init__(white=white)
        self.color()
        self.name += "king"

    def positions_can_move(self, spots, start):
        self.positions.clear()
        for i in range(-1, 2):
            for j in range(-1, 2):
                x, y = start.x + i, start.y + j
                if self.inside_board(x, y):
                    if spots[y][x].piece.is_white != self.is_white:
                        self.positions.append((start, spots[y][x]))
  
    def get_img(self):
        if self.is_white:
            return WHITE_KING
        return BLACK_KING

class Pawn(Piece):
    def __init__(self, white=None):
        super().__init__(white=white)
        self.color()
        self.name += "pawn"

    def positions_can_move(self, spots, start):
        self.positions.clear()
        if self.is_white:
            direction = -1
            jump = 6
        else:
            direction = 1
            jump = 1
        if start.y == jump:
            if spots[start.y + direction * 2][start.x].piece.is_white == None:
                if spots[start.y + direction][start.x].piece.is_white == None:
                    self.positions.append((start, spots[start.y + direction * 2][start.x]))
        if start.y + direction >= 0 and start.y + direction <= 7:
            if spots[start.y + direction][start.x].piece.is_white == None:
                self.positions.append((start, spots[start.y + direction][start.x]))
            if start.x + 1 <= 7:
                if spots[start.y + direction][start.x + 1].piece.is_white == (not self.is_white):
                    self.positions.append((start, spots[start.y + direction][start.x + 1]))
            if start.x - 1 >= 0:
                if spots[start.y + direction][start.x - 1].piece.is_white == (not self.is_white):
                    self.positions.append((start, spots[start.y + direction][start.x - 1]))
            
    def get_img(self):
        if self.is_white:
            return WHITE_PAWN
        return BLACK_PAWN
