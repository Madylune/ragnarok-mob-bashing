import pygame

class Potion(object):
  # image = pygame.image.load('assets/item/potion.png')

  def __init__(self,x,y, width, height):
    self.x = x
    self.y = y
    self.width
    self.height
    self.isVisible = False

  def draw(self, window):
    # window.blit(self.image, (self.x, self.y))
    if self.isVisible:
      pygame.draw.circle(window, (255,0,0), self.x, self.y)
