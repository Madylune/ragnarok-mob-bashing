import pygame

class Coldbolt(pygame.sprite.Sprite):
  def __init__(self, player):
    super().__init__()
    self.velocity = 15
    self.player = player
    self.image = pygame.image.load('assets/skill/coldbolt.png')
    self.image = pygame.transform.scale(self.image, (20, 80))
    self.image = pygame.transform.rotate(self.image, 20)
    self.rect = self.image.get_rect()
    self.rect.x = player.rect.x + 100
    self.rect.y = player.rect.y - 250

  def remove(self):
    self.player.all_spells.remove(self)

  def move(self):
    self.rect.y += self.velocity
    self.rect.x += (self.velocity - 10)

    # Check collision with monster
    for monster in self.player.game.check_collision(self, self.player.game.monsters_group):
      self.remove()
      monster.damage(self.player.attack, 'water')
      
    for monster in self.player.game.check_collision(self, self.player.game.boss_group):
      self.remove()
      monster.damage(self.player.attack, 'water')

    # Remove projectile outside
    if self.rect.x > 800:
      self.remove()
    if self.rect.y > 320:
      self.remove()