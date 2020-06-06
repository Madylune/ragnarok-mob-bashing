import pygame
import random
from components.player import Player
from components.monster import Monster
from components.boss import Boss
from components.bar import Bar
from components.indicator import Indicator

MONSTERS_TO_KILL = 10

class Game:
  def __init__(self):
    self.is_playing = False
    self.player_titles = ['mage', 'wizard', 'high wizard']
    self.player_title = self.player_titles[0]
    self.player = Player(self)
    self.players_group = pygame.sprite.Group(self.player)
    self.monsters_group = pygame.sprite.Group()
    self.boss_group = pygame.sprite.Group()
    self.bar = Bar(self.player)
    self.levels = ['payon', 'morroc', 'geffen', 'island', 'yuno', 'veins', 'abbeye']
    self.level_index = 0
    self.map_index = 1
    self.current_level = self.levels[self.level_index]
    self.killed_monters = 0 
    self.killed_boss = 0
    self.points = 0
    self.all_indicators = pygame.sprite.Group()
    # Get pressed keys
    self.pressed = {}

  def show_indicators(self):
    indicator = Indicator(self)
    self.all_indicators.add(indicator)

  def pop_monsters(self):
    self.spawn_monster(0)
    self.spawn_monster(1)
    self.spawn_monster(2)
    self.spawn_monster(3)

  def start(self):
    pygame.mixer.music.unload()
    self.is_playing = True
    self.pop_monsters()

  def next_map(self):
    pygame.mixer.music.unload()
    self.map_index += 1
    self.killed_monters = 0
    if self.map_index > 3:
      self.next_level()
    else:
      self.killed_monters = 0
      self.killed_boss = 0
      self.monsters_group = pygame.sprite.Group()
      self.boss_group = pygame.sprite.Group()
      self.pop_monsters()

  def next_level(self):
    pygame.mixer.music.unload()
    self.map_index = 1
    self.level_index += 1
    if self.level_index >= len(self.levels):
      self.game_over()
    else:
      self.killed_monters = 0
      self.killed_boss = 0
      self.current_level = self.levels[self.level_index]
      self.monsters_group = pygame.sprite.Group()
      self.boss_group = pygame.sprite.Group()
      self.pop_monsters()

  def game_over(self):
    pygame.mixer.music.unload()
    self.monsters_group = pygame.sprite.Group()
    self.boss_group = pygame.sprite.Group()
    self.player.health = self.player.max_health
    self.is_playing = False

  def update(self, screen):
    self.players_group.draw(screen)
    self.bar.update_health_bar(screen)
    self.bar.update_exp_bar(screen)

    if self.player.level <= 1:
      self.player_title = self.player_titles[0]
    if self.player.level > 1 and self.player.level <= 2:
      self.player_title = self.player_titles[1]
      self.player.swap_image('wizard')
    if self.player.level > 2:
      self.player_title = self.player_titles[2]
      self.player.swap_image('hw')

    if self.map_index <= 3 and self.killed_monters >= MONSTERS_TO_KILL:
      if len(self.boss_group) < 1:
        self.spawn_boss()
      elif self.killed_boss == 1:
        self.next_map()
    
    if self.map_index == 3 and self.killed_monters >= MONSTERS_TO_KILL:
      if len(self.boss_group) < 1:
        self.spawn_boss()
      elif self.killed_boss == 1:
        self.next_level()

    # Player's moving
    if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
      self.player.move_right()
    elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
      self.player.move_left()

    for indicator in self.all_indicators:
      indicator.move()

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
    self.all_indicators.draw(screen)

  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

  def spawn_monster(self, mob):
    monster = Monster(self, mob)
    self.monsters_group.add(monster)

  def spawn_boss(self):
    boss = Boss(self)
    self.boss_group.add(boss)
