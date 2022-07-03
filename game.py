import datetime
import os
import random
import threading

import pygame

from const import SCREEN_HEIGHT, SCREEN_WIDTH, \
    SCREEN, RUN_IMAGE, \
    JUMP_IMAGE, DUCK_IMAGE, \
    DEAD_IMAGE, FLOOR

from Dino import Dino

pygame.init()

pygame.display.set_caption('Dino Game')

ICON = pygame.image.load('assets/Icon.png')
pygame.display.set_icon(ICON)

def main():
    global game_speed, x_pos_bg, y_pos_bg
    run = True
    clock = pygame.time.Clock()
    player = Dino()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 400

    def background():
        global x_pos_bg, y_pos_bg
        image_width = FLOOR.get_width()
        SCREEN.blit(FLOOR, (x_pos_bg, y_pos_bg))
        SCREEN.blit(FLOOR, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(FLOOR, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                run = False

        SCREEN.fill((255, 255, 255))

        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        background()
        pygame.display.update()

        clock.tick(40)


def menu(death_count):
    run = True

    while run:
        SCREEN.fill((255, 255, 255))

        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Press any key dear", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(ICON, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                main()


t1 = threading.Thread(target=menu(death_count=0), daemon=True)
t1.start()
