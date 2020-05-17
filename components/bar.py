import pygame

class Bar(object):
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def drawHp(self, window, player):
    pygame.draw.rect(window, (75,97,11), (self.x, self.y, self.width, self.height))
    if player.hp > 0:
      pygame.draw.rect(window, (58,223,0), (self.x, self.y, (player.hp * 2), self.height))

  def drawSp(self, window, player):
    pygame.draw.rect(window, (11,56,97), (self.x, self.y, self.width, self.height))
    if player.sp > 0:
      pygame.draw.rect(window, (1,116,223), (self.x, self.y, (player.sp * 2), self.height))
