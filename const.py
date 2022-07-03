import os
import pygame

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUN_IMAGE = [
    pygame.image.load(os.path.join('assets/Dino/Run1.png')),
    pygame.image.load(os.path.join('assets/Dino/Run2.png'))
]

JUMP_IMAGE = pygame.image.load(os.path.join('assets/Dino/Jump.png'))

DUCK_IMAGE = [
    pygame.image.load(os.path.join('assets/Dino/Duck1.png')),
    pygame.image.load(os.path.join('assets/Dino/Duck2.png'))
]

DEAD_IMAGE = pygame.image.load(os.path.join('assets/Dino/Dead.png'))

FLOOR = pygame.image.load(os.path.join('assets/Floor.png'))
