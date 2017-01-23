import pygame

class Hero(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 20
        #self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load("hero.jpg")
        self.rect = self.image.get_rect()
        #self.image.fill((255,0,0))



    def move(self):
        yPos = pygame.mouse.get_pos()[1]
        self.rect.y = yPos