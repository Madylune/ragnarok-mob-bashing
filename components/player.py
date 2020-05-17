import pygame

class Player(object):
  standing = pygame.image.load('assets/player/standing.png')
  dying = pygame.image.load('assets/player/Rdead.png')
  sitting = pygame.image.load('assets/player/sitting.png')
  onHitRight = pygame.image.load('assets/player/RonHit.png')
  onHitLeft = pygame.image.load('assets/player/LonHit.png')
  walkRight = [pygame.image.load('assets/player/R1.png'), pygame.image.load('assets/player/R2.png'), pygame.image.load('assets/player/R3.png'), pygame.image.load('assets/player/R4.png'), pygame.image.load('assets/player/R5.png'), pygame.image.load('assets/player/R6.png'), pygame.image.load('assets/player/R7.png'), pygame.image.load('assets/player/R8.png')]
  walkLeft = [pygame.image.load('assets/player/L1.png'), pygame.image.load('assets/player/L2.png'), pygame.image.load('assets/player/L3.png'), pygame.image.load('assets/player/L4.png'), pygame.image.load('assets/player/L5.png'), pygame.image.load('assets/player/L6.png'), pygame.image.load('assets/player/L7.png'), pygame.image.load('assets/player/L8.png')]


  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.speed = 5
    self.isJumping = False
    self.left = False
    self.right = False
    self.standing = True
    self.walkCount = 0
    self.jumpCount = 10
    self.hitbox = (self.x, self.y, self.width, self.height)
    self.hitting = False
    self.hp = 100
    self.sp = 100
    self.dead = False
    self.isSitting = False
  
  def draw(self, window):
    # print('hp:', self.hp)
    # pygame.draw.rect(window, (255,0,0), self.hitbox, 2)

    if not (self.dead):
      # 8 images * 3 times each animation 
      if self.walkCount + 1 >= 24: 
        self.walkCount = 0

      if not (self.standing):
        if self.left:
          window.blit(self.walkLeft[self.walkCount//3], (self.x,self.y)) #//: Résultat entier d'une division
          self.walkCount += 1
        elif self.right:
          window.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
          self.walkCount += 1
      elif self.isSitting:
        window.blit(self.sitting, (self.x, self.y + 20))
      elif self.hitting:
        if self.left:
          window.blit(self.onHitLeft, (self.x, self.y))
        else:
          window.blit(self.onHitRight, (self.x, self.y))
      else:
        if self.right:
          window.blit(self.walkRight[0], (self.x, self.y))
        else:
          window.blit(self.walkLeft[0], (self.x, self.y))
      self.hitbox = (self.x, self.y, self.width, self.height)
    else:
      window.blit(self.dying, (self.x, self.y))


  def hit(self, window):
    if self.hp > 0:
      self.hitting = True
      self.isJumping = False
      self.isSitting = False
      self.jumpCount = 10
      self.y = 300
      self.walkCount = 0
      self.hp -= 10
      if self.right:
        self.x -= 100
      else: 
        self.x += 100
    else:
      self.dead = True

    pygame.display.update()
