import pygame

class Boss(pygame.sprite.Sprite):
  def __init__(self, game):
    super(Boss, self).__init__()
    self.game = game

    self.images = []
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L4.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L4.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/boss/L4.png'))

    self.index = 0
    self.image = self.images[self.index]

    self.rect = self.image.get_rect()
    self.rect.x = 800

    self.health = 200
    self.max_health = 200
    self.velocity = 0.1
    self.defense = 2
    
    if self.game.current_level == 'payon':
      if self.game.map_index == 1: #eddga
        self.rect.y = 260
        self.attack = 2
        self.health_bar_rect_x = -30
        self.health_bar_rect_y = -20
        self.points = 200
      if self.game.map_index == 2: #moonlight
        self.rect.y = 260
        self.attack = 3
        self.health_bar_rect_x = -30
        self.health_bar_rect_y = -20
        self.points = 200
      if self.game.map_index == 3: #baphomet
        self.rect.y = 240
        self.attack = 4
        self.health_bar_rect_x = -10
        self.health_bar_rect_y = -20
        self.points = 300

    if self.game.current_level == 'morroc':
      if self.game.map_index == 1: #phreeoni
        self.rect.y = 240
        self.attack = 6
        self.health_bar_rect_x = -20
        self.health_bar_rect_y = -20
        self.points = 200
      if self.game.map_index == 2: #maya
        self.rect.y = 250
        self.attack = 7
        self.health_bar_rect_x = -35
        self.health_bar_rect_y = -20
        self.points = 200
      if self.game.map_index == 3: #pharaoh
        self.rect.y = 240
        self.attack = 8
        self.health_bar_rect_x = -50
        self.health_bar_rect_y = -20
        self.points = 400

    if self.game.current_level == 'geffen':
      if self.game.map_index == 1: #gtb
        self.rect.y = 270
        self.attack = 9
        self.health_bar_rect_x = -20
        self.health_bar_rect_y = - 20
        self.points = 200
      if self.game.map_index == 2: #orc lord
        self.rect.y = 250
        self.attack = 10
        self.health_bar_rect_x = -35
        self.health_bar_rect_y = -20
        self.points = 300
      if self.game.map_index == 3: #dark lord
        self.rect.y = 200
        self.attack = 11
        self.health_bar_rect_x = -25
        self.health_bar_rect_y = -10
        self.points = 500

    if self.game.current_level == 'island':
      if self.game.map_index == 1: #octopus
        self.rect.y = 240
        self.attack = 12
        self.health_bar_rect_x = -20
        self.health_bar_rect_y = -20
        self.points = 400
      if self.game.map_index == 2: #drake
        self.rect.y = 240
        self.attack = 13
        self.health_bar_rect_x = -40
        self.health_bar_rect_y = -20
        self.points = 300
      if self.game.map_index == 3: #turtle general
        self.rect.y = 245
        self.attack = 14
        self.health_bar_rect_x = -25
        self.health_bar_rect_y = -20
        self.points = 500

    if self.game.current_level == 'yuno':
      if self.game.map_index == 1: #atroce
        self.rect.y = 250
        self.attack = 15
        self.health_bar_rect_x = -25
        self.health_bar_rect_y = -20
        self.points = 600
      if self.game.map_index == 2: #rsx
        self.rect.y = 230
        self.attack = 16
        self.health_bar_rect_x = -25
        self.health_bar_rect_y = -20
        self.points = 600
      if self.game.map_index == 3: #vesper
        self.rect.y = 245
        self.attack = 17
        self.health_bar_rect_x = -30
        self.health_bar_rect_y = -20
        self.points = 700

    if self.game.current_level == 'veins':
      if self.game.map_index == 1: #detareudus
        self.rect.y = 260
        self.attack = 18
        self.health_bar_rect_x = -15
        self.health_bar_rect_y = -20
        self.points = 500
      if self.game.map_index == 2: #ktullanux
        self.rect.y = 230
        self.attack = 19
        self.health_bar_rect_x = -30
        self.health_bar_rect_y = -5
        self.points = 700
      if self.game.map_index == 3: #ifrit
        self.rect.y = 205
        self.attack = 20
        self.health_bar_rect_x = -20
        self.health_bar_rect_y = -10
        self.points = 700

    if self.game.current_level == 'abbeye':
      if self.game.map_index == 1: #lord of the dead
        self.rect.y = 230
        self.attack = 21
        self.health_bar_rect_x = -15
        self.health_bar_rect_y = -25
        self.points = 200
      if self.game.map_index == 2: #fallen bishop
        self.rect.y = 250
        self.attack = 22
        self.health_bar_rect_x = -40
        self.health_bar_rect_y = -5
        self.points = 600
      if self.game.map_index == 3: #valkyrie
        self.rect.y = 240
        self.attack = 23
        self.health_bar_rect_x = 0
        self.health_bar_rect_y = -10
        self.points = 800

  def die(self):
    self.game.boss_group.remove(self)

  def damage(self, amount, element):
    self.health -= (amount / self.defense)

    if self.health <= 0:
      self.game.killed_boss += 1
      self.game.player.update_exp(self.points)
      self.die()

  def update_health_bar(self, surface):
    pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + self.health_bar_rect_x, self.rect.y + self.health_bar_rect_y, self.max_health, 7])
    pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + self.health_bar_rect_x, self.rect.y + self.health_bar_rect_y, self.health, 7])

  def forward(self):
    if not self.game.check_collision(self, self.game.players_group):
      self.rect.x -= self.velocity
      self.index += 1
      if self.index >= len(self.images):
        self.index = 0
      self.image = self.images[self.index]
    else:
      self.game.player.damage(self.attack)