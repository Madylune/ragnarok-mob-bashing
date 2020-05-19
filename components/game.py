import pygame
from components.player import Player
from components.monster import Monster
from components.bar import Bar

class Game:
  def __init__(self):
    self.is_playing = False
    self.player = Player(self)
    self.players_group = pygame.sprite.Group(self.player)
    self.monsters_group = pygame.sprite.Group()
    self.bar = Bar(self.player)
    # Get pressed keys
    self.pressed = {}

  def start(self):
    self.is_playing = True
    # Generate monsters when initialization
    self.spawn_monster()
    self.spawn_monster()

  def game_over(self):
    # Reset game
    self.monsters_group = pygame.sprite.Group()
    self.player.health = self.player.max_health
    self.is_playing = False

  def update(self, screen):
    self.players_group.draw(screen)
    self.bar.update_health_bar(screen)

    # Player's moving
    if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
      self.player.move_right()
    elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
      self.player.move_left()

    for spell in self.player.all_spells:
      spell.move()
    
    for monster in self.monsters_group:
      monster.forward()
      # pygame.draw.rect(screen, (255,0,0), monster.rect, 2)
      monster.update_health_bar(screen)

    self.player.all_spells.draw(screen)
    self.monsters_group.draw(screen)

  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

  def spawn_monster(self):
    monster = Monster(self)
    self.monsters_group.add(monster)
