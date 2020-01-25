import pygame
import time

class Monster(object):
  onHitRight = pygame.image.load('assets/RonHitE.png')
  onHitLeft = pygame.image.load('assets/LonHitE.png')
  walkRight = [pygame.image.load('assets/R1E.png'), pygame.image.load('assets/R2E.png'), pygame.image.load('assets/R3E.png'), pygame.image.load('assets/R4E.png'), pygame.image.load('assets/R5E.png'), pygame.image.load('assets/R6E.png'), pygame.image.load('assets/R7E.png'), pygame.image.load('assets/R8E.png')]
  walkLeft = [pygame.image.load('assets/L1E.png'), pygame.image.load('assets/L2E.png'), pygame.image.load('assets/L3E.png'), pygame.image.load('assets/L4E.png'), pygame.image.load('assets/L5E.png'), pygame.image.load('assets/L6E.png'), pygame.image.load('assets/L7E.png'), pygame.image.load('assets/L8E.png')]

  def __init__(self, x, y, width, height, end):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.end = end
    self.path = [self.x, self.end]
    self.walkCount = 0
    self.speed = 3
    self.hitbox = (self.x, self.y, 100, 150) #(top left x, top left y, width, height)
    self.health = 100
    self.visible = True
    self.hitting = False

  def draw(self, window):
    self.move()
    if self.visible: 
      if self.walkCount + 1 >= 24:
        self.walkCount = 0
      
      if self.hitting:
        if self.speed > 0:
          window.blit(self.onHitLeft, (self.x, self.y))
        else:
          window.blit(self.onHitRight, (self.x, self.y))
      else:
        if self.speed > 0:
          window.blit(pygame.transform.scale(self.walkRight[self.walkCount //3], (120, 150)), (self.x, self.y))
          self.walkCount += 1 
        else:
          window.blit(pygame.transform.scale(self.walkLeft[self.walkCount //3], (120, 150)), (self.x, self.y))
          self.walkCount += 1 

      pygame.draw.rect(window, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 100, 10))
      pygame.draw.rect(window, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20,  self.health, 10))
      self.hitbox = (self.x, self.y, 100, 150)

  def move(self):
    if self.speed > 0:
      if self.x + self.speed < self.path[1]:
        self.x += self.speed
      else:
        self.speed = self.speed * -1
        self.walkCount = 0
    else:
      if self.x - self.speed > self.path[0]:
        self.x += self.speed
      else:
        self.speed = self.speed * -1
        self.walkCount = 0

  def hit(self):
    # self.hitting = True
    if self.health > 0:
      self.health -= 10
    else:
      self.visible = False
