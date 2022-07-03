from const import SCREEN_WIDTH


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, obstacles_list, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles_list.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], (self.rect.x, self.rect.y - 40))
