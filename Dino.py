import pygame
from const import SCREEN_HEIGHT, SCREEN_WIDTH, \
    SCREEN, RUN_IMAGE, \
    JUMP_IMAGE, DUCK_IMAGE, \
    DEAD_IMAGE, TRACK


class Dino:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

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

        # if (userInput[pygame.K_UP] or userInput[pygame.K_SPACE]) and not self.dino_jump:
        #     self.dino_jump = True
        #     self.dino_duck = False
        #     self.dino_run = False
        # elif userInput[pygame.K_DOWN] and not self.dino_jump:
        #     self.dino_jump = False
        #     self.dino_duck = True
        #     self.dino_run = False
        # elif not (userInput[pygame.K_DOWN] or self.dino_jump):
        #     self.dino_jump = False
        #     self.dino_duck = False
        self.dino_run = True

    def run(self):
        self.image = self.run_image[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        pass

    def crouch(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
