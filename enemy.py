import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10
        self.enemy = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.rect = self.enemy.get_rect()
        self.speedx = 7
        self.speedy = 4



    def move(self):
        self.rect.x -= self.speedx


