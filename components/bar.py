import pygame

class Bar(pygame.sprite.Sprite):
  def __init__(self, player):
    super().__init__()
    self.player = player

  def update_health_bar(self, surface):
    font = pygame.font.SysFont('comicsans', 27, True)
    text = font.render('HP', 1, (0,0,0))
    surface.blit(text, (0,5))
    pygame.draw.rect(surface, (60, 63, 60), [30, 5, (self.player.max_health * 2), 20])
    pygame.draw.rect(surface, (111, 210, 46), [30, 5, (self.player.health * 2), 20])
