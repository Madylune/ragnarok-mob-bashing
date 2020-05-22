import pygame
import random
from components.player import Player
from components.monster import Monster
from components.boss import Boss
from components.bar import Bar

class Game:
  def __init__(self):
    self.is_playing = False
    self.player = Player(self)
    self.players_group = pygame.sprite.Group(self.player)
    self.monsters_group = pygame.sprite.Group()
    self.boss_group = pygame.sprite.Group()
    self.bar = Bar(self.player)
    self.levels = ['payon', 'morroc', 'starry', 'einbech', 'abyss', 'odin']
    self.index = 0
    self.current_level = self.levels[self.index]
    self.killed_monters = 0 
    self.killed_boss = 0
    # Get pressed keys
    self.pressed = {}

  def pop_monsters(self):
    self.spawn_monster(0)
    self.spawn_monster(1)
    self.spawn_monster(2)
    self.spawn_monster(3)

  def start(self):
    self.is_playing = True
    self.pop_monsters()

  def pass_level(self):
    self.index += 1
    if self.index >= len(self.levels):
      self.game_over()
    else:
      self.killed_monters = 0
      self.killed_boss = 0
      self.current_level = self.levels[self.index]
      self.monsters_group = pygame.sprite.Group()
      self.boss_group = pygame.sprite.Group()
      self.pop_monsters()

  def game_over(self):
    # Reset game
    self.monsters_group = pygame.sprite.Group()
    self.boss_group = pygame.sprite.Group()
    self.player.health = self.player.max_health
    self.is_playing = False

  def update(self, screen):
    self.players_group.draw(screen)
    self.bar.update_health_bar(screen)

    if self.killed_monters >= 5 and len(self.boss_group) < 1:
      self.monsters_group = pygame.sprite.Group()
      self.spawn_boss()

    if self.killed_boss == 1:
      self.pass_level()

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

    for boss in self.boss_group:
      boss.forward()
      boss.update_health_bar(screen)

    self.player.all_spells.draw(screen)
    self.monsters_group.draw(screen)
    self.boss_group.draw(screen)

  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

  def spawn_monster(self, mob):
    monster = Monster(self, mob)
    self.monsters_group.add(monster)

  def spawn_boss(self):
    boss = Boss(self)
    self.boss_group.add(boss)
