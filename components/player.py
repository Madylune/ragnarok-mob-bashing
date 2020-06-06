import pygame
from components.fireball import Fireball
from components.lightbolt import Lightbolt
from components.coldbolt import Coldbolt

class Player(pygame.sprite.Sprite):
  def __init__(self, game):
    super(Player, self).__init__()
    self.game = game
    self.title = 'hw' if self.game.player_title == 'high wizard' else self.game.player_title
    self.images_right = []
    self.images_left = []
    i = 1
    while i < 8:
      self.images_right.append(pygame.image.load('assets/player/' + self.title + '/R' + str(i) + '.png'))
      self.images_left.append(pygame.image.load('assets/player/' + self.title + '/L' + str(i) + '.png'))
      i += 1

    #index value to get the image from the array, initially it is 0 
    self.index = 0
    self.image = self.images_right[self.index]
    self.rect = pygame.Rect(350, 300, 45, 110)
    self.velocity = 5 # Moving speed
    self.attack = 10
    self.all_spells = pygame.sprite.Group()
    self.health = 100
    self.max_health = 100
    self.exp = 0
    self.max_exp = 800
    self.level = 0

  def swap_image(self, title):
    self.images_right = []
    self.images_left = []
    i = 1
    while i < 8:
      self.images_right.append(pygame.image.load('assets/player/' + title + '/R' + str(i) + '.png'))
      self.images_left.append(pygame.image.load('assets/player/' + title + '/L' + str(i) + '.png'))
      i += 1

    self.image = self.images_right[self.index]
    
  def update_exp(self, amount):
    if self.exp >= self.max_exp:
      self.level += 1
      self.exp = 0
    else:
      self.exp += amount

  def damage(self, amount):
    if self.health - amount > amount:
      self.health -= amount
    else:
      self.game.game_over()

  def move_right(self):
    if not self.game.check_collision(self, self.game.boss_group):
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
    