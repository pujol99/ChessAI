import os
import pygame

class Image:
    def __init__(self):
        self.board = pygame.image.load(os.path.abspath('imgs/board.png'))
        #load all images
        self.start = pygame.image.load(os.path.abspath('imgs/selected_orign.png'))
        self.objective = pygame.image.load(os.path.abspath('imgs/objective.png'))
        self.attack = pygame.image.load(os.path.abspath('imgs/attack.png'))
        self.bTower = pygame.image.load(os.path.abspath('imgs/blackTower.png'))
        self.bHorse = pygame.image.load(os.path.abspath('imgs/blackHorse.png'))
        self.bBishop = pygame.image.load(os.path.abspath('imgs/blackBishop.png'))
        self.bKing = pygame.image.load(os.path.abspath('imgs/blackKing.png'))
        self.bQueen = pygame.image.load(os.path.abspath('imgs/blackQueen.png'))
        self.bPawn = pygame.image.load(os.path.abspath('imgs/blackPawn.png'))
        self.wTower = pygame.image.load(os.path.abspath('imgs/whiteTower.png'))
        self.wHorse = pygame.image.load(os.path.abspath('imgs/whiteHorse.png'))
        self.wBishop = pygame.image.load(os.path.abspath('imgs/whiteBishop.png'))
        self.wKing = pygame.image.load(os.path.abspath('imgs/whiteKing.png'))
        self.wQueen = pygame.image.load(os.path.abspath('imgs/whiteQueen.png'))
        self.wPawn = pygame.image.load(os.path.abspath('imgs/whitePawn.png'))
        #load colors
        self.bg = pygame.Color('0x000000')