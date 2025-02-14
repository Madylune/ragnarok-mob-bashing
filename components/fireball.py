import pygame

class Fireball(pygame.sprite.Sprite):
  def __init__(self, player):
    super().__init__()
    self.velocity = 10
    self.player = player
    self.image = pygame.image.load('assets/skill/fireball.png')
    self.image = pygame.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()
    self.rect.x = player.rect.x + 20
    self.rect.y = player.rect.y + 40
    self.origin_image = self.image
    self.angle = 0

  def rotate(self):
    self.angle += 8
    self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
    self.rect = self.image.get_rect(center=self.rect.center)

  def remove(self):
    self.player.all_spells.remove(self)

  def move(self):
    self.rect.x += self.velocity
    self.rotate()

    # Check collision with monster
    for monster in self.player.game.check_collision(self, self.player.game.monsters_group):
      self.remove()
      monster.damage(self.player.attack, 'fire')

    for monster in self.player.game.check_collision(self, self.player.game.boss_group):
      self.remove()
      monster.damage(self.player.attack, 'fire')

    # Remove projectile outside
    if self.rect.x > 800 or self.rect.x > (self.player.rect.x + 250):
      self.remove()