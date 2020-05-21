import pygame
import random

class Monster(pygame.sprite.Sprite):
  def __init__(self, game, mob):
    super(Monster, self).__init__()
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

    self.game = game
    self.health = 100
    self.max_health = 100
    self.mobs_attacks = [0.5, 0.1, 0.3] #bigfoot / poring / willow
    self.attack = self.mobs_attacks[mob]
    self.rect = self.image.get_rect()
    self.rect.x = 800 + random.randint(0, 200)
    self.mobs_rect_y = [300, 370, 340]
    self.rect.y = self.mobs_rect_y[mob]
    self.velocity = random.randint(1, 3)

  def respawn(self):
    self.rect.x = 1000 + random.randint(0, 300)
    self.velocity = random.randint(1, 3)
    self.health = self.max_health

  def damage(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.respawn()
      self.game.killed_monters += 1

  def update_health_bar(self, surface):
    if self.mob == 0: #bigfoot
      pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.max_health, 7])
      pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 20, self.health, 7])

    if self.mob == 1: #poring
      pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 25, self.rect.y - 15, self.max_health, 7])
      pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 25, self.rect.y - 15, self.health, 7])

    if self.mob == 2: #willow
      pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 20, self.rect.y - 15, self.max_health, 7])
      pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 20, self.rect.y - 15, self.health, 7])

  def forward(self):
    if not self.game.check_collision(self, self.game.players_group):
      self.rect.x -= self.velocity
      self.index += 1
      if self.index >= len(self.images):
        self.index = 0
      self.image = self.images[self.index]
    else:
      self.game.player.damage(self.attack)
      