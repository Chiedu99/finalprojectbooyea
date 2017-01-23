import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, width, height, speedx, ):
        super().__init__()
        self.Width = width
        self.Height = height
        self.image = pygame.Surface((self.Width, self.Height))
        self.rect = self.image.get_rect()
        self.speedx = speedx


    def move(self):
        self.rect.x -= self.speedx


