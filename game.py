import pygame
import random
import threading

from Dino.Dino import Dino
from Obstacle.Cactus import SmallCactus, LargeCactus
from const import SCREEN_HEIGHT, SCREEN_WIDTH, \
    SCREEN, FLOOR, \
    SMALL_CACTUS, LARGE_CACTUS

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
    obstacles_list = []
    death_count = 0

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

        if len(obstacles_list) == 0:
            if random.randint(0, 2) == 0:
                obstacles_list.append(SmallCactus(SMALL_CACTUS))
            if random.randint(0, 2) == 1:
                obstacles_list.append(LargeCactus(LARGE_CACTUS))

        for obstacle in obstacles_list:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles_list, game_speed)

            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

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
