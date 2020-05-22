import pygame
from components.fireball import Fireball
from components.lightbolt import Lightbolt
from components.coldbolt import Coldbolt

class Player(pygame.sprite.Sprite):
  def __init__(self, game):
    super(Player, self).__init__()
    self.images_right = []
    self.images_right.append(pygame.image.load('assets/player/R1.png'))
    self.images_right.append(pygame.image.load('assets/player/R2.png'))
    self.images_right.append(pygame.image.load('assets/player/R3.png'))
    self.images_right.append(pygame.image.load('assets/player/R4.png'))
    self.images_right.append(pygame.image.load('assets/player/R5.png'))
    self.images_right.append(pygame.image.load('assets/player/R6.png'))
    self.images_right.append(pygame.image.load('assets/player/R7.png'))
    self.images_right.append(pygame.image.load('assets/player/R8.png'))

    self.images_left = []
    self.images_left.append(pygame.image.load('assets/player/L1.png'))
    self.images_left.append(pygame.image.load('assets/player/L2.png'))
    self.images_left.append(pygame.image.load('assets/player/L3.png'))
    self.images_left.append(pygame.image.load('assets/player/L4.png'))
    self.images_left.append(pygame.image.load('assets/player/L5.png'))
    self.images_left.append(pygame.image.load('assets/player/L6.png'))
    self.images_left.append(pygame.image.load('assets/player/L7.png'))
    self.images_left.append(pygame.image.load('assets/player/L8.png'))

    #index value to get the image from the array, initially it is 0 
    self.index = 0
    self.image = self.images_right[self.index]
    self.rect = pygame.Rect(350, 300, 45, 110)
    self.velocity = 5 # Moving speed
    self.attack = 10
    self.all_spells = pygame.sprite.Group()
    self.game = game
    self.health = 100
    self.max_health = 100

  def damage(self, amount):
    if self.health - amount > amount:
      self.health -= amount
    else:
      self.game.game_over()

  def move_right(self):
    if not self.game.check_collision(self, self.game.monsters_group) or not self.game.check_collision(self, self.game.boss_group):
      self.rect.x += self.velocity 
      self.index += 1
      if self.index >= len(self.images_right):
        self.index = 0
      self.image = self.images_right[self.index]

  def move_left(self):
    self.rect.x -= self.velocity
    self.index += 1
    if self.index >= len(self.images_left):
      self.index = 0
    self.image = self.images_left[self.index]

  def cast_spell(self, element):
    if element == 'fire':
      self.all_spells.add(Fireball(self))
    if element == 'wind':
      self.all_spells.add(Lightbolt(self))
    if element == 'water':
      self.all_spells.add(Coldbolt(self))
    