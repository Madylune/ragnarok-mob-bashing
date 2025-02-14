import pygame
import random

class Monster(pygame.sprite.Sprite):
  def __init__(self, game, mob):
    super(Monster, self).__init__()
    self.game = game
    self.mob = mob
    self.images = []
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/mob' + str(mob) + '/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/mob' + str(mob) + '/L1.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/mob' + str(mob) + '/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/mob' + str(mob) + '/L2.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/mob' + str(mob) + '/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/mob' + str(mob) + '/L3.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/mob' + str(mob) + '/L4.png'))
    self.images.append(pygame.image.load('assets/mobs/' + game.current_level + '/' + game.current_level + str(game.map_index) + '/mob' + str(mob) + '/L4.png'))

    self.index = 0
    self.image = self.images[self.index]

    self.health = 100
    self.max_health = 100
    self.rect = self.image.get_rect()
    self.rect.x = 800 + random.randint(0, 100)

    self.mobs_points = []
    self.mobs_elements = []
    self.mobs_attacks = [] 
    self.mobs_defense = []
    self.mobs_rect_y = []
    self.mobs_health_bar_rect_x = []
    self.mobs_health_bar_rect_y = []

    if self.game.current_level == 'payon':
      if self.game.map_index == 1:
        self.mobs_rect_y = [300, 370, 340, 350] #bigfoot / poring / willow / spore
        self.mobs_attacks = [0.5, 0.1, 0.2, 0.3]
        self.mobs_defense = [3, 0, 0.5, 1] 
        self.mobs_elements = ['fire', 'wind', 'fire', 'wind']
        self.mobs_health_bar_rect_x = [-10, -25, -20, -20]
        self.mobs_health_bar_rect_y = [-20, -15, -15, -15]
        self.mobs_points = [50, 10, 60, 70]
      if self.game.map_index == 2:
        self.mobs_rect_y = [325, 320, 290, 350] #zombie / skeleton / sohee / ninetail
        self.mobs_attacks = [0.2, 0.4, 0.5, 0.5] 
        self.mobs_defense = [1.5, 1, 2, 2]
        self.mobs_elements = ['fire', 'fire', 'wind', 'water']
        self.mobs_health_bar_rect_x = [-20, -20, 0, -20]
        self.mobs_health_bar_rect_y = [-20, -15, -15, -15]
        self.mobs_points = [80, 60, 80, 80]
      if self.game.map_index == 3:
        self.mobs_rect_y = [300, 360, 365, 345] #rocker / argos / smokie / baphometJr
        self.mobs_attacks = [0.3, 0.5, 0.4, 0.7]
        self.mobs_defense = [1, 1, 1, 3]
        self.mobs_elements = ['fire', 'neutral', 'fire', 'holy']
        self.mobs_health_bar_rect_x = [-20, -10, -20, -20]
        self.mobs_health_bar_rect_y = [-20, -20, -15, -15]
        self.mobs_points = [20, 50, 30, 80]

    if self.game.current_level == 'morroc':
      if self.game.map_index == 1:
        self.mobs_rect_y = [330, 370, 320, 340] #muka / drops / peco / wolf
        self.mobs_attacks = [0.5, 0.1, 0.5, 0.7]
        self.mobs_defense = [2, 0, 2, 2.5]
        self.mobs_elements = ['fire', 'water', 'water', 'fire']
        self.mobs_health_bar_rect_x = [-25, -25, -20, 0]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [80, 10, 70, 100]
      if self.game.map_index == 2:
        self.mobs_rect_y = [365, 365, 365, 365] #andre / deniro / piere / vitata
        self.mobs_attacks = [0.2, 0.2, 0.2, 0.5]
        self.mobs_defense = [1, 1, 1, 1.5]
        self.mobs_elements = ['fire', 'fire', 'fire', 'fire']
        self.mobs_health_bar_rect_x = [-20, -20, -20, -20]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [20, 20, 20, 50]
      if self.game.map_index == 3:
        self.mobs_rect_y = [250, 270, 320, 340] #anubis / minorous / mummy / verit
        self.mobs_attacks = [1, 0.7, 0.9, 0.6]
        self.mobs_defense = [5, 3, 4, 1.8]
        self.mobs_elements = ['fire', 'water', 'fire', 'fire']
        self.mobs_health_bar_rect_x = [10, 10, -15, -20]
        self.mobs_health_bar_rect_y = [-15, -20, -15, -15]
        self.mobs_points = [150, 120, 100, 90]

    if self.game.current_level == 'geffen':
      if self.game.map_index == 1:
        self.mobs_rect_y = [300, 380, 370, 350] #familiar / tarou / thief bug male / poison spore
        self.mobs_attacks = [0.2, 0.2, 0.5, 0.6]
        self.mobs_defense = [0, 0, 1, 1.5]
        self.mobs_elements = ['holy', 'holy', 'holy', 'neutral']
        self.mobs_health_bar_rect_x = [-20, -30, -20, -20]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [30, 20, 50, 70]
        
      if self.game.map_index == 2:
        self.mobs_rect_y = [310, 320, 350, 320] #orc warrior / orc lady / orc baby / orc archer
        self.mobs_attacks = [0.8, 0.8, 0.6, 0.9]
        self.mobs_defense = [2, 2, 1, 2]
        self.mobs_elements = ['fire', 'fire', 'fire', 'fire']
        self.mobs_health_bar_rect_x = [-10, -10, -30, -20]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [80, 80, 70, 90]
      if self.game.map_index == 3:
        self.mobs_rect_y = [305, 275, 140, 310] #dark priest / wraith / AK / raydric
        self.mobs_attacks = [1.7, 1, 2.5, 1.5]
        self.mobs_defense = [6, 3, 7, 5]
        self.mobs_elements = ['fire', 'fire', 'holy', 'holy']
        self.mobs_health_bar_rect_x = [-20, -20, 50, -25]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [60, 30, 80, 70]

    if self.game.current_level == 'island':
      if self.game.map_index == 1:
        self.mobs_rect_y = [330, 340, 340, 190] #obeaune / thara / marc / strouf
        self.mobs_attacks = [0.8, 0.4, 0.7, 1]
        self.mobs_defense = [2, 1, 1.5, 2.5]
        self.mobs_elements = ['wind', 'wind', 'wind', 'wind']
        self.mobs_health_bar_rect_x = [-20, -25, -20, 0]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [20, 10, 40, 70]
      if self.game.map_index == 2:
        self.mobs_rect_y = [315, 320, 330, 340] #pirate skeleton / whisper / hydra / penomena
        self.mobs_attacks = [1, 0.7, 0.5, 1.5]
        self.mobs_defense = [2, 1, 0.5, 2.5]
        self.mobs_elements = ['fire', 'ghost', 'wind', 'neutral']
        self.mobs_health_bar_rect_x = [-20, -30, -15, -10]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [70, 30, 20, 80]
      if self.game.map_index == 3:
        self.mobs_rect_y = [300, 315, 350, 335] #dragon tail / spring rabbit / freezer / permeter
        self.mobs_attacks = [1.7, 1.6, 1.9, 1.9]
        self.mobs_defense = [3, 3, 5, 5]
        self.mobs_elements = ['earth', 'fire', 'wind', 'neutral']
        self.mobs_health_bar_rect_x = [-15, -20, -15, -15]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [80, 80, 90, 90]

    if self.game.current_level == 'yuno':
      if self.game.map_index == 1:
        self.mobs_rect_y = [350, 315, 240, 325] #geographer / grand peco / harpy / goat
        self.mobs_attacks = [0.8, 0.9, 1.2, 1]
        self.mobs_defense = [2, 2.5, 3, 2.5]
        self.mobs_elements = ['fire', 'water', 'earth', 'water']
        self.mobs_health_bar_rect_x = [-20, -10, 10, 0]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [30, 35, 50, 10]
      if self.game.map_index == 2:
        self.mobs_rect_y = [350, 370, 310, 360] #giearth / metaling / pitman / teddy bear
        self.mobs_attacks = [0.7, 0.5, 1, 1.5]
        self.mobs_defense = [2, 1.5, 2.5, 3]
        self.mobs_elements = ['fire', 'fire', 'fire', 'neutral']
        self.mobs_health_bar_rect_x = [-20, -25, 0, -25]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [10, 10, 40, 50]
      if self.game.map_index == 3:
        self.mobs_rect_y = [320, 350, 295, 295] #dimik / venatu / archdam / apocalypse
        self.mobs_attacks = [2, 1.7, 1.9, 2.7]
        self.mobs_defense = [5, 4, 5, 7]
        self.mobs_elements = ['neutral', 'neutral', 'neutral', 'neutral']
        self.mobs_health_bar_rect_x = [-5, -20, 0, 0]
        self.mobs_health_bar_rect_y = [-15, -15, -5, -15]
        self.mobs_points = [20, 20, 30, 50]

    if self.game.current_level == 'veins':
      if self.game.map_index == 1:
        self.mobs_rect_y = [330, 310, 310, 275] #ancient mimic / green ferus / red ferus / hydrolancer
        self.mobs_attacks = [1, 1.5, 1.5, 3]
        self.mobs_defense = [5, 6, 6, 8]
        self.mobs_elements = ['neutral', 'fire', 'water', 'holy']
        self.mobs_health_bar_rect_x = [15, 0, 0, 15]
        self.mobs_health_bar_rect_y = [-20, -15, -15, -15]
        self.mobs_points = [10, 20, 20, 60]
      if self.game.map_index == 2:
        self.mobs_rect_y = [350, 270, 260, 260] #siroma / gazeti / snowier / ice titan
        self.mobs_attacks = [1, 1.5, 1.8, 2.5]
        self.mobs_defense = [2, 3, 3, 5]
        self.mobs_elements = ['wind', 'wind', 'wind', 'wind']
        self.mobs_health_bar_rect_x = [-5, 5, 10, 45]
        self.mobs_health_bar_rect_y = [-15, -15, -5, -15]
        self.mobs_points = [10, 20, 30, 50]
      if self.game.map_index == 3:
        self.mobs_rect_y = [200, 280, 320, 305] #kasa / salamander / imp / kaho
        self.mobs_attacks = [3, 3.5, 2.5, 2]
        self.mobs_defense = [6, 7, 4, 2]
        self.mobs_elements = ['water', 'water', 'water', 'water']
        self.mobs_health_bar_rect_x = [25, 25, 0, -20]
        self.mobs_health_bar_rect_y = [-5, 0, 0, -15]
        self.mobs_points = [20, 30, 50, 10]

    if self.game.current_level == 'abbeye':
      if self.game.map_index == 1:
        self.mobs_rect_y = [290, 305, 340, 270] #gibbet / dullahan / lude / loli ruri
        self.mobs_attacks = [0.7, 1.2, 0.5, 1.9]
        self.mobs_defense = [1.5, 2, 0, 2.5]
        self.mobs_elements = ['holy', 'fire', 'fire', 'holy']
        self.mobs_health_bar_rect_x = [-5, -5, -20, -5]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [10, 15, 5, 20]
      if self.game.map_index == 2:
        self.mobs_rect_y = [235, 265, 250, 235] #Zombie Slaughter / Flame Skull / Banshee / Necromancer
        self.mobs_attacks = [2.5, 2, 2.7, 3]
        self.mobs_defense = [4, 4, 5, 6]
        self.mobs_elements = ['fire', 'ghost', 'holy', 'fire']
        self.mobs_health_bar_rect_x = [30, 10, 20, 30]
        self.mobs_health_bar_rect_y = [20, 10, -5, 10]
        self.mobs_points = [20, 10, 30, 50]
      if self.game.map_index == 3:
        self.mobs_rect_y = [310, 370, 300, 300] #skogul / skeggiold / plasma / frus
        self.mobs_attacks = [2, 3, 1.5, 2]
        self.mobs_defense = [6, 8, 2, 6]
        self.mobs_elements = ['holy', 'dark', 'water', 'holy']
        self.mobs_health_bar_rect_x = [-20, -25, -20, -20]
        self.mobs_health_bar_rect_y = [-15, -15, -15, -15]
        self.mobs_points = [40, 50, 10, 40]
    
    self.points = self.mobs_points[mob]
    self.attack = self.mobs_attacks[mob]
    self.defense = self.mobs_defense[mob]
    self.rect.y = self.mobs_rect_y[mob]
    self.element = self.mobs_elements[mob]
    self.health_bar_rect_x = self.mobs_health_bar_rect_x[mob]
    self.health_bar_rect_y = self.mobs_health_bar_rect_y[mob]
    self.velocity = random.randint(1, 5)

  def respawn(self):
    self.rect.x = 800 + random.randint(0, 300)
    self.velocity = random.randint(1, 3)
    self.health = self.max_health

  def die(self):
    self.game.drop_potion(self, random.randint(0, 1))
    self.respawn()
    self.game.killed_monters += 1
    self.game.player.update_exp(self.points)

  def damage(self, amount, element):
    damages = amount - self.defense
    if element == self.element:
      self.health -= (damages * 2)
    else:
      self.health -= damages

    if self.health <= 0:
      self.die()

  def update_health_bar(self, surface):
    pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + self.health_bar_rect_x, self.rect.y + self.health_bar_rect_y, self.max_health, 7])
    pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + self.health_bar_rect_x, self.rect.y + self.health_bar_rect_y, self.health, 7])

  def forward(self):
    if self.rect.x < 0:
      self.respawn()

    if not self.game.check_collision(self, self.game.players_group):
      self.rect.x -= self.velocity
      self.index += 1
      if self.index >= len(self.images):
        self.index = 0
      self.image = self.images[self.index]
    else:
      self.game.player.damage(self.attack)
      