import pygame

class Bar(pygame.sprite.Sprite):
  def __init__(self, player):
    super().__init__()
    self.player = player

  def update_health_bar(self, surface):
    pygame.draw.rect(surface, (60, 63, 60), [60, 25, (self.player.max_health * 2), 20])
    pygame.draw.rect(surface, (111, 210, 46), [60, 25, (self.player.health * 2), 20])
