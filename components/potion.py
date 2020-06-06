import pygame

class Potion(pygame.sprite.Sprite):
  def __init__(self, game, x):
    super().__init__()
    self.game = game
    self.x = x
    self.image = pygame.image.load('assets/potion.png')
    self.image = pygame.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = 375

  def pick_up(self):
    pick_up_sound = pygame.mixer.Sound('assets/sounds/pickup.wav')
    pygame.mixer.Sound.play(pick_up_sound)
    self.game.all_potions.remove(self)
    self.game.add_potion()

  def drop(self):
    self.rect.x = self.x

    if self.game.check_collision(self, self.game.players_group):
      self.pick_up()

    