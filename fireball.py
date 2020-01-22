import pygame

class Fireball(object):
  imageRight = pygame.image.load('assets/Rfireball.png')
  imageLeft = pygame.image.load('assets/Lfireball.png')
  imageRight = pygame.transform.scale(imageRight, (50, 30))
  imageLeft = pygame.transform.scale(imageLeft, (50, 30))

  def __init__(self,x,y,facing):
    self.x = x
    self.y = y
    self.facing = facing
    self.speed = 8 * facing

  def draw(self, window):
    if self.facing == 1:
      window.blit(self.imageRight, (self.x, self.y))
    else:
      window.blit(self.imageLeft, (self.x, self.y))
