import pygame
from const import SCREEN_HEIGHT, SCREEN_WIDTH, \
    SCREEN, RUN_IMAGE, \
    JUMP_IMAGE, DUCK_IMAGE, \
    DEAD_IMAGE, FLOOR


class Dino:
    X_POS = 100
    Y_POS = 340
    Y_POS_DUCK = 390
    JUMP_VEL = 7.5

    def __init__(self):
        self.run_image = RUN_IMAGE
        self.duck_image = DUCK_IMAGE
        self.jump_image = JUMP_IMAGE

        self.dino_run = False
        self.dino_duck = False
        self.dino_jump = False

        self.image = self.run_image[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL

    def update(self, userInput):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0

        if (userInput[pygame.K_UP] or userInput[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def run(self):
        self.image = self.run_image[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_image
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.dino_rect.y >= self.Y_POS:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x + 45, self.dino_rect.y))
