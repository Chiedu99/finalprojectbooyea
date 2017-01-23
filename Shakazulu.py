import pygame
import enemy


class Shakazulu(enemy.Enemy):
    def __init__(self):
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 15
        #self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load("shakazulu.png")
        self.rect = self.image.get_rect()
        self.speedx = 7


    def move(self):
        self.rect.x -= self.speedx
