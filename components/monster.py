import pygame
import time
import random

class Monster(object):
  walkRight = [pygame.image.load('assets/mob/R1E1.png'), pygame.image.load('assets/mob/R2E1.png'), pygame.image.load('assets/mob/R3E1.png'), pygame.image.load('assets/mob/R4E1.png'), pygame.image.load('assets/mob/R5E1.png'), pygame.image.load('assets/mob/R6E1.png'), pygame.image.load('assets/mob/R7E1.png'), pygame.image.load('assets/mob/R8E1.png')]
  walkLeft = [pygame.image.load('assets/mob/L1E1.png'), pygame.image.load('assets/mob/L2E1.png'), pygame.image.load('assets/mob/L3E1.png'), pygame.image.load('assets/mob/L4E1.png'), pygame.image.load('assets/mob/L5E1.png'), pygame.image.load('assets/mob/L6E1.png'), pygame.image.load('assets/mob/L7E1.png'), pygame.image.load('assets/mob/L8E1.png')]

  def __init__(self, x, y, width, height, end):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.end = end
    self.path = [self.x, self.end]
    self.walkCount = 0
    self.speed = 3
    self.hitbox = (self.x, self.y, self.width, self.height) #(top left x, top left y, width, height)
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
          window.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
          self.walkCount += 1 
        else:
          window.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
          self.walkCount += 1 

      pygame.draw.rect(window, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 100, 10))
      pygame.draw.rect(window, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20,  self.health, 10))
      self.hitbox = (self.x, self.y, self.width, self.height)
      # pygame.draw.rect(window, (255,0,0), self.hitbox, 2)

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
      self.health -= random.randint(10, 30)
    else:
      self.visible = False
