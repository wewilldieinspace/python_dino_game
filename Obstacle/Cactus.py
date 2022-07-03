import random
from Obstacle.Obstacle import Obstacle


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 4)
        super().__init__(image, self.type)
        self.rect.y = 360


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 4)
        super().__init__(image, self.type)
        self.rect.y = 335
