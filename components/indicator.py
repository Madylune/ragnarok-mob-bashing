import pygame

class Indicator(pygame.sprite.Sprite):
  def __init__(self, game):
    super().__init__()
    self.game = game
    self.velocity = 5
    self.image = pygame.image.load('assets/levelup.png')
    self.image = pygame.transform.scale(self.image, (100, 70))
    self.rect = self.image.get_rect()
    self.rect.x = game.player.rect.x - 35
    self.rect.y = game.player.rect.y - 30

  def remove(self):
    self.game.all_indicators.remove(self)

  def move(self):
    self.rect.y -= self.velocity

    if self.rect.y < 200:
      self.remove()