import pygame
import random

class Monster(pygame.sprite.Sprite):
  def __init__(self, game):
    super(Monster, self).__init__()
    self.images = []
    self.images.append(pygame.image.load('assets/mob/2/L1.png'))
    self.images.append(pygame.image.load('assets/mob/2/L2.png'))
    self.images.append(pygame.image.load('assets/mob/2/L3.png'))
    self.images.append(pygame.image.load('assets/mob/2/L4.png'))
    self.images.append(pygame.image.load('assets/mob/2/L5.png'))
    self.images.append(pygame.image.load('assets/mob/2/L6.png'))
    self.images.append(pygame.image.load('assets/mob/2/L7.png'))

    self.index = 0
    self.image = self.images[self.index]

    self.game = game
    self.health = 100
    self.max_health = 100
    self.attack = 0.3
    self.rect = self.image.get_rect()
    self.rect.x = 800 + random.randint(0, 200)
    self.rect.y = 300
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
    pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.max_health, 7])
    pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 20, self.health, 7])

  def forward(self):
    if not self.game.check_collision(self, self.game.players_group):
      self.rect.x -= self.velocity
      self.index += 1
      if self.index >= len(self.images):
        self.index = 0
      self.image = self.images[self.index]
    else:
      self.game.player.damage(self.attack)
      