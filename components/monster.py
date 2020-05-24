import pygame
import random

class Monster(pygame.sprite.Sprite):
  def __init__(self, game, mob):
    super(Monster, self).__init__()
    self.game = game
    self.mob = mob
    self.images = []
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/mob' + str(mob) + '/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/mob' + str(mob) + '/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/mob' + str(mob) + '/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/mob' + str(mob) + '/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/mob' + str(mob) + '/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/mob' + str(mob) + '/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/mob' + str(mob) + '/L4.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/mob' + str(mob) + '/L4.png'))

    self.index = 0
    self.image = self.images[self.index]

    self.health = 100
    self.max_health = 100
    self.rect = self.image.get_rect()
    self.rect.x = 800 + random.randint(0, 100)

    self.mobs_elements = []
    self.mobs_attacks = [] 
    self.mobs_rect_y = []

    if self.game.current_level == 'payon':
      self.mobs_rect_y = [300, 370, 340, 350] #bigfoot / poring / willow / spore
      self.mobs_attacks = [0.5, 0.1, 0.2, 0.3] 
      self.mobs_elements = ['fire', 'wind', 'fire', 'wind']

    if self.game.current_level == 'morroc':
      self.mobs_rect_y = [330, 370, 320, 340] #muka / drops / peco / wolf
      self.mobs_attacks = [0.5, 0.1, 0.5, 0.7]
      self.mobs_elements = ['fire', 'water', 'water', 'fire']

    if self.game.current_level == 'island':
      self.mobs_rect_y = [330, 340, 340, 190] #obeaune / thara / marc / strouf
      self.mobs_attacks = [0.8, 0.4, 0.7, 1]
      self.mobs_elements = ['wind', 'wind', 'wind', 'wind']

    if self.game.current_level == 'yuno':
      self.mobs_rect_y = [350, 370, 310, 360] #giearth / metaling / pitman / teddy bear
      self.mobs_attacks = [0.7, 0.5, 1, 1.5]
      self.mobs_elements = ['fire', 'fire', 'fire', 'neutral']

    if self.game.current_level == 'veins':
      self.mobs_rect_y = [330, 310, 310, 275] #ancient mimic / green ferus / red ferus / hydrolancer
      self.mobs_attacks = [1, 1.5, 1.5, 3]
      self.mobs_elements = ['neutral', 'fire', 'water', 'holy']

    if self.game.current_level == 'abbeye':
      self.mobs_rect_y = [310, 370, 300, 300] #skogul / skeggiold / plasma / frus
      self.mobs_attacks = [2, 3, 1.5, 2]
      self.mobs_elements = ['holy', 'dark', 'water', 'holy']
    
    self.attack = self.mobs_attacks[mob]
    self.rect.y = self.mobs_rect_y[mob]
    self.element = self.mobs_elements[mob]
    self.velocity = random.randint(1, 5)

  def respawn(self):
    self.rect.x = 800 + random.randint(0, 300)
    self.velocity = random.randint(1, 3)
    self.health = self.max_health

  def damage(self, amount, element):
    if element == self.element:
      self.health -= (amount * 2)
    else:
      self.health -= amount

    if self.health <= 0:
      self.respawn()
      self.game.killed_monters += 1

  def update_health_bar(self, surface):
    if self.mob == 0: 
      if self.game.current_level == 'payon': #bigfoot
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 20, self.health, 7])
      elif self.game.current_level == 'morroc': #muka
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 25, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 25, self.rect.y - 15, self.health, 7])
      elif self.game.current_level == 'veins': #ancient mimic
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y - 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y - 20, self.health, 7])
      else: #obeaune, giearth, skoguld
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 20, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 20, self.rect.y - 15, self.health, 7])

    elif self.mob == 1:
      if self.game.current_level == 'veins': #green ferus
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 15, self.health, 7])
      else: #poring, drops, thara, metaling, skeggiold
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 25, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 25, self.rect.y - 15, self.health, 7])

    elif self.mob == 2:
      if self.game.current_level == 'yuno' or self.game.current_level == 'veins': #pitman, red ferus
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 15, self.health, 7])
      else: #willow, peco, marc, plasma
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 20, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 20, self.rect.y - 15, self.health, 7])

    elif self.mob == 3:
      if self.game.current_level == 'payon': #spore
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 20, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 20, self.rect.y - 15, self.health, 7])
      elif self.game.current_level == 'yuno': #teddy
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 25, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 25, self.rect.y - 15, self.health, 7])
      elif self.game.current_level == 'veins': #hydro
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y - 15, self.health, 7])
      else: #wolf, strouf
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 15, self.health, 7])
  
  def forward(self):
    if self.rect.x < 0:
      self.respawn()

    if not self.game.check_collision(self, self.game.players_group):
      self.rect.x -= self.velocity
      self.index += 1
      if self.index >= len(self.images):
        self.index = 0
      self.image = self.images[self.index]
    else:
      self.game.player.damage(self.attack)
      