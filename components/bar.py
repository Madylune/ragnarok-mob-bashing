import pygame

class Bar(pygame.sprite.Sprite):
  def __init__(self, player):
    super().__init__()
    self.player = player

  def update_health_bar(self, surface):
    pygame.draw.rect(surface, (60, 63, 60), [60, 25, (self.player.max_health * 2), 20])
    pygame.draw.rect(surface, (111, 210, 46), [60, 25, (self.player.health * 2), 20])

  def update_exp_bar(self, surface):
    pygame.draw.rect(surface, (217, 240, 255), [0, surface.get_height() - 12, self.player.max_exp, 12])
    pygame.draw.rect(surface, (0, 136, 231), [0, surface.get_height() - 12, self.player.exp, 12])

    pygame.draw.line(surface, (97, 97, 97), (self.player.max_exp / 4, surface.get_height() - 15), ((self.player.max_exp / 4), surface.get_height()), 2)
    pygame.draw.line(surface, (97, 97, 97), (self.player.max_exp / 2, surface.get_height() - 15), ((self.player.max_exp / 2), surface.get_height()), 2)
    pygame.draw.line(surface, (97, 97, 97), (self.player.max_exp - (self.player.max_exp / 4), surface.get_height() - 15), (self.player.max_exp - (self.player.max_exp / 4), surface.get_height()), 2)