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

SMALL_CACTUS = [
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Small1.png")),
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Small2.png")),
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Small3.png")),
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Small4.png")),
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Small5.png"))
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Large1.png")),
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Large2.png")),
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Large3.png")),
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Large4.png")),
    pygame.image.load(os.path.join("assets/Obstacle/Cactus", "Large5.png")),
]

DEAD_IMAGE = pygame.image.load(os.path.join('assets/Dino/Dead.png'))

FLOOR = pygame.image.load(os.path.join('assets/Floor.png'))
