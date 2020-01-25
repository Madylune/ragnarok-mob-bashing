import pygame

class Player(object):
  standing = pygame.image.load('assets/standing.png')
  dying = pygame.image.load('assets/Rdead.png')
  onHitRight = pygame.image.load('assets/RonHit.png')
  onHitLeft = pygame.image.load('assets/LonHit.png')
  walkRight = [pygame.image.load('assets/R1.png'), pygame.image.load('assets/R2.png'), pygame.image.load('assets/R3.png'), pygame.image.load('assets/R4.png'), pygame.image.load('assets/R5.png'), pygame.image.load('assets/R6.png'), pygame.image.load('assets/R7.png'), pygame.image.load('assets/R8.png')]
  walkLeft = [pygame.image.load('assets/L1.png'), pygame.image.load('assets/L2.png'), pygame.image.load('assets/L3.png'), pygame.image.load('assets/L4.png'), pygame.image.load('assets/L5.png'), pygame.image.load('assets/L6.png'), pygame.image.load('assets/L7.png'), pygame.image.load('assets/L8.png')]


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
    self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    self.hitting = False
    self.hp = 100
    self.sp = 50
    self.dead = False
  
  def draw(self, window):
    # print('hp:', self.hp)

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
      self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    else:
      window.blit(self.dying, (self.x, self.y))


  def hit(self, window):
    if self.hp > 0:
      self.hitting = True
      self.isJumping = False
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
