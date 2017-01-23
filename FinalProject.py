import pygame
import enemy
import hero
import ultrode
import Shakazulu
import meruem
import prpjectile
import random
from pygame.locals import *
import sys

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
APPLICATION_WIDTH = 400
APPLICATION_HEIGHT = 600
NUM_TURNS= 4
SCORE = 0
MAX= 450
pygame.init()
mainSurface = pygame.display.set_mode((1000, MAX), 0, 32)
increasespeed = False
currentscore = SCORE
mainSurface.fill(WHITE)
hero1 = hero.Hero()
hero1.rect.x = 0
hero1.rect.y = APPLICATION_HEIGHT/2
mainSurface.blit(hero1.image, hero1.rect)
ultrode1 = ultrode.Ultrode()
shakazulu1 = Shakazulu.Shakazulu()
shakazulu1.rect.x = 1100
shakazulu1.rect.y = random.randint(1,200)
ultrode1.rect.x = 1100
ultrode1.rect.y = random.randint(1,400)
mainSurface.blit(ultrode1.image, ultrode1.rect)
meruem1 = meruem.Meruem()
meruem1.rect.x = 1100
meruem1.rect.y = random.randint(1,650)
mainSurface.blit(meruem1.image, meruem1.rect)
projectileU = prpjectile.Projectile(10, 10, 15)
projectileU.rect.x = ultrode1.rect.x
projectileU.rect.y = ultrode1.rect.y
projectileS = prpjectile.Projectile(20, 15, 10)
projectileS.rect.x = shakazulu1.rect.x
projectileS.rect.y = shakazulu1.rect.y
projectileM = prpjectile.Projectile(15, 5, 20)
projectileM.rect.x = meruem1.rect.x
projectileM.rect.y = meruem1.rect.y
ultrode2 = ultrode.Ultrode()
shakazulu2 = Shakazulu.Shakazulu()
shakazulu2.rect.x = 1100
shakazulu2.rect.y = random.randint(1,200)
ultrode2.rect.x = 1100
ultrode2.rect.y = random.randint(1,400)
mainSurface.blit(ultrode2.image, ultrode2.rect)
meruem2 = meruem.Meruem()
meruem2.rect.x = 1100
meruem2.rect.y = random.randint(1,650)
mainSurface.blit(meruem2.image, meruem2.rect)
projectileU2 = prpjectile.Projectile(10, 10, 15)
projectileU2.rect.x = ultrode2.rect.x
projectileU2.rect.y = ultrode2.rect.y
projectileS2 = prpjectile.Projectile(20, 15, 10)
projectileS2.rect.x = shakazulu2.rect.x
projectileS2.rect.y = shakazulu2.rect.y
projectileM2 = prpjectile.Projectile(15, 5, 20)
projectileM2.rect.x = meruem2.rect.x
projectileM2.rect.y = meruem2.rect.y



pygame.display.update()
enemyGroup= pygame.sprite.Group()
enemyGroup.add(ultrode1)
enemyGroup.add(shakazulu1)
enemyGroup.add(meruem1)
enemyGroup.add(ultrode2)
enemyGroup.add(shakazulu2)
enemyGroup.add(meruem2)
projectileGroup = pygame.sprite.Group()
projectileGroup.add(projectileU)
projectileGroup.add(projectileS)
projectileGroup.add(projectileM)
projectileGroup.add(projectileU2)
projectileGroup.add(projectileS2)
projectileGroup.add(projectileM2)
heroGroup = pygame.sprite.Group()
heroGroup.add(hero1)



while True:
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
  mainSurface.fill(WHITE)

  for enemy in enemyGroup:
      enemy.move()
      if shakazulu1.rect.right < 0:
          shakazulu1.rect.x = random.randint(1000,1200)
          shakazulu1.rect.y = random.randint(1, MAX)
          SCORE += 1

      if ultrode1.rect.right < 0:
          ultrode1.rect.x =  random.randint(1000,1200)
          ultrode1.rect.y = random.randint(1, MAX)
          SCORE += 1

      if meruem1.rect.right < 0:
          meruem1.rect.x =  random.randint(1000,1200)
          meruem1.rect.y = random.randint(1, MAX)
          SCORE += 1

      if shakazulu2.rect.right < 0:
          shakazulu2.rect.x = random.randint(1000, 1200)
          shakazulu2.rect.y = random.randint(1, MAX)
          SCORE += 1

      if ultrode2.rect.right < 0:
          ultrode2.rect.x = random.randint(1000, 1200)
          ultrode2.rect.y = random.randint(1, MAX)
          SCORE += 1

      if meruem2.rect.right < 0:
          meruem2.rect.x = random.randint(1000, 1200)
          meruem2.rect.y = random.randint(1, MAX)
          SCORE += 1




      mainSurface.blit(enemy.image, enemy.rect)

  for projectile in projectileGroup:
      projectile.move()
      if projectileM.rect.right < -150:
          projectileM.rect.x = meruem1.rect.x
          projectileM.rect.y = meruem1.rect.y


      if projectileU.rect.right < -150:
          projectileU.rect.x = ultrode1.rect.x
          projectileU.rect.y = ultrode1.rect.y

      if projectileS.rect.right < -150:
          projectileS.rect.x = shakazulu1.rect.x
          projectileS.rect.y = shakazulu1.rect.y

      if projectileM2.rect.right < -150:
          projectileM2.rect.x = meruem2.rect.x
          projectileM2.rect.y = meruem2.rect.y


      if projectileU2.rect.right < -150:
          projectileU2.rect.x = ultrode2.rect.x
          projectileU2.rect.y = ultrode2.rect.y

      if projectileS2.rect.right < -150:
          projectileS2.rect.x = shakazulu2.rect.x
          projectileS2.rect.y = shakazulu2.rect.y

      mainSurface.blit(projectile.image, projectile.rect)

      for projectile in projectileGroup:
          if pygame.sprite.spritecollide(projectileU, heroGroup, False):
              projectileU.rect.x = ultrode1.rect.x
              projectileU.rect.y = ultrode1.rect.y
              NUM_TURNS -= 1
          if pygame.sprite.spritecollide(projectileM, heroGroup, False):
              projectileM.rect.x = meruem1.rect.x
              projectileM.rect.y = meruem1.rect.y
              NUM_TURNS -= 1
          if pygame.sprite.spritecollide(projectileS, heroGroup, False):
              projectileS.rect.x = shakazulu1.rect.x
              projectileS.rect.y = shakazulu1.rect.y
              NUM_TURNS -= 1
          if pygame.sprite.spritecollide(projectileU, heroGroup, False):
              projectileU2.rect.x = ultrode2.rect.x
              projectileU2.rect.y = ultrode2.rect.y
              NUM_TURNS -= 1
          if pygame.sprite.spritecollide(projectileM, heroGroup, False):
              projectileM2.rect.x = meruem2.rect.x
              projectileM2.rect.y = meruem2.rect.y
              NUM_TURNS -= 1
          if pygame.sprite.spritecollide(projectileS, heroGroup, False):
              projectileS2.rect.x = shakazulu2.rect.x
              projectileS2.rect.y = shakazulu2.rect.y
              NUM_TURNS -= 1
          if SCORE % 20 == 0 and SCORE != 0:
              increasespeed = True
              currentscore = SCORE

          if currentscore != SCORE and increasespeed:
                currentscore = 20
                projectileM.speedx += 2
                projectileS.speedx += 2
                projectileU.speedx += 2
                projectileM2.speedx += 2
                projectileS2.speedx += 2
                projectileU2.speedx += 2
                shakazulu1.speedx += 2
                meruem1.speedx += 2
                ultrode1.speedx += 2
                shakazulu2.speedx += 2
                ultrode2.speedx += 2
                meruem2.speedx += 2
                increasespeed = False





  hero1.move()
  mainSurface.blit(hero1.image, hero1.rect)
  print(NUM_TURNS)
  print(SCORE)

  if NUM_TURNS <= 0:
      pygame.quit()
      sys.exit()
  pygame.display.update()


