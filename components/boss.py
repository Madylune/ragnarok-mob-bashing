import pygame

class Boss(pygame.sprite.Sprite):
  def __init__(self, game):
    super(Boss, self).__init__()
    self.game = game

    self.images = []
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L4.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L4.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/boss/L4.png'))

    self.index = 0
    self.image = self.images[self.index]

    self.rect = self.image.get_rect()
    self.rect.x = 800
    self.rect.y = 250

    self.health = 200
    self.max_health = 200
    self.velocity = 0.1
    self.attack = 2
    self.defense = 2

  def die(self):
    self.game.boss_group.remove(self)

  def damage(self, amount, element):
    self.health -= (amount / self.defense)

    if self.health <= 0:
      self.game.killed_boss += 1
      self.die()

  def update_health_bar(self, surface):
    pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 35, self.rect.y - 20, self.max_health, 7])
    pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 35, self.rect.y - 20, self.health, 7])

  def forward(self):
    if not self.game.check_collision(self, self.game.players_group):
      self.rect.x -= self.velocity
      self.index += 1
      if self.index >= len(self.images):
        self.index = 0
      self.image = self.images[self.index]
    else:
      self.game.player.damage(self.attack)