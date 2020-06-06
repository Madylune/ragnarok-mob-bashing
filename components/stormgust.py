import pygame

class Stormgust(pygame.sprite.Sprite):
  def __init__(self, player):
    super().__init__()
    self.velocity = 5
    self.player = player
    self.image = pygame.image.load('assets/skill/stormgust.png')
    self.rect = self.image.get_rect()
    self.rect.x = player.rect.x - 200
    self.rect.y = player.rect.y - 180

  def remove(self):
    self.player.all_spells.remove(self)

  def move(self):
    self.rect.y += self.velocity
    self.rect.x += (self.velocity - 2)

    # Check collision with monster
    for monster in self.player.game.check_collision(self, self.player.game.monsters_group):
      monster.damage(self.player.attack, 'water')

    for monster in self.player.game.check_collision(self, self.player.game.boss_group):
      monster.damage(self.player.attack, 'water')

    # Remove projectile outside
    if self.rect.y > 350:
      self.remove()