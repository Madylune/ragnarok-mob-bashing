import pygame

class Monster(object):
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
    self.hitbox = (self.x + 17, self.y + 2, 31, 57)
    self.health = 10
    self.visible = True

  def draw(self, window):
    self.move()
    if self.visible: 
      if self.walkCount + 1 >= 24:
        self.walkCount = 0
      
      if self.speed > 0:
        window.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
        self.walkCount += 1 
      else:
        window.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
        self.walkCount += 1 

      pygame.draw.rect(window, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
      pygame.draw.rect(window, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
      self.hitbox = (self.x + 17, self.y + 2, 31, 57)

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
    if self.health > 0:
      self.health -= 1
    else:
      self.visible = False
