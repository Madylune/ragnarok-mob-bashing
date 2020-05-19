import pygame

class Lightbolt(pygame.sprite.Sprite):
  def __init__(self, player):
    super().__init__()
    self.velocity = 15
    self.player = player
    self.image = pygame.image.load('assets/skill/lightbolt.png')
    self.image = pygame.transform.scale(self.image, (100, 100))
    self.rect = self.image.get_rect()
    self.rect.x = player.rect.x + 100
    self.rect.y = player.rect.y - 250
    self.origin_image = self.image
    self.angle = 0

  def remove(self):
    self.player.all_spells.remove(self)

  def move(self):
    self.rect.y += self.velocity

    # Check collision with monster
    for monster in self.player.game.check_collision(self, self.player.game.monsters_group):
      self.remove()
      monster.damage(self.player.attack)

    # Remove projectile outside
    if self.rect.x > 800:
      self.remove()
    if self.rect.y > 320:
      self.remove()