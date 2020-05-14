import pygame
import random
from player import Player
from fireball import Fireball
from monster import Monster
from boss import Boss
from bar import Bar

SCREEN_WIDTH = 900

class SceneBase:
  def __init__(self):
    self.next = self
    
  def ProcessInput(self, events, pressed_keys):
    # Receive all events that happened since the last frame
    pass

  def Update(self):
    # Put your game logic in here for the scene
    pass

  def Render(self, screen):
    # Render code, will receive the main screen Surface as input
    pass

  def SwitchToScene(self, next_scene):
    self.next = next_scene

  def Terminate(self):
    self.SwitchToScene(None)

class GameScene(SceneBase):
  player = Player(300, 300, 45, 100)
  boss = Boss(random.randint(100, 500), 260, 120, 150, random.randint(500, 700))
  hp = Bar(30, 5, 200, 20)
  sp = Bar(30, 30, 200, 20)
  bullets = []
  shootLoop = 0
  facing = -1
  mobs = []
  new_mob = Monster(random.randint(100, 500), 300, 65, 100, random.randint(500, 700))
  mobs.append(new_mob)

  def __init__(self):
    SceneBase.__init__(self)

  def ProcessInput(self, events, pressed_keys):
    #----- EVENTS ----#
    PLAYER_REGEN_SP = pygame.USEREVENT + 1
    MONSTER_POP = pygame.USEREVENT + 2
    for event in pygame.event.get():
      if event.type == PLAYER_REGEN_SP:
        if self.player.sp < 100 and self.player.sp < self.sp.width:
          self.player.sp += 10  
      
      elif event.type == MONSTER_POP:
        new_mob = Monster(random.randint(100, 500), 300, 65, 100, random.randint(500, 700))
        mobs.append(new_mob)

    #----- PRESSED KEYS ----#
    if not (self.player.dead):
      if pressed_keys[pygame.K_SPACE] and self.shootLoop == 0:
        # pygame.time.set_timer(MONSTER_POP, 5000)
        self.player.hitting = False
        if self.player.sp > 0:
          # fireballSound.play()
          fireball = Fireball(round(self.player.x + self.player.width//2), round(self.player.y + self.player.height//2), self.facing)
          self.player.sp -= 15
          if len(self.bullets) < 5:
            self.bullets.append(fireball)
          self.shootLoop = 1

      if pressed_keys[pygame.K_LEFT] and self.player.x > self.player.speed:
        pygame.time.set_timer(PLAYER_REGEN_SP, 0)
        self.player.hitting = False
        self.player.x -= self.player.speed
        self.player.left = True
        self.player.right = False
        self.player.standing = False
        self.player.isSitting = False
        self.facing = -1
      elif pressed_keys[pygame.K_RIGHT] and self.player.x < SCREEN_WIDTH - self.player.width - self.player.speed:
        pygame.time.set_timer(PLAYER_REGEN_SP, 0)
        self.player.hitting = False
        self.player.x += self.player.speed
        self.player.left = False
        self.player.right = True
        self.player.standing = False
        self.player.isSitting = False
        self.facing = 1
      else:
        self.player.standing = True
        self.player.walkCount = 0
      
      if not (self.player.isJumping):
        if pressed_keys[pygame.K_UP]:
          self.player.hitting = False
          self.player.isJumping = True
          self.player.right = False
          self.player.left = False
          self.player.walkCount = 0
          self.player.isSitting = False
        elif pressed_keys[pygame.K_DOWN]:
          pygame.time.set_timer(PLAYER_REGEN_SP, 1000)
          self.player.hitting = False
          self.player.isJumping = False
          self.player.right = False
          self.player.left = False
          self.player.isSitting = True
          self.player.walkCount = 0
      else:
        if self.player.jumpCount >= -10:
          neg = 1
          if self.player.jumpCount < 0:
            neg = -1
          self.player.y -= (self.player.jumpCount ** 2) * 0.5 * neg
          self.player.jumpCount -= 1
        else:
          self.player.isJumping = False
          self.player.jumpCount = 10

  def Update(self):
    pass
    # for mob in mobs:
    #   if mob.visible == True:
    #     if self.player.hitbox[1] < mob.hitbox[1] + mob.hitbox[3] and self.player.hitbox[1] + self.player.hitbox[3] > mob.hitbox[1]:
    #       if self.player.hitbox[0] + self.player.hitbox[2] > mob.hitbox[0] and self.player.hitbox[0] < mob.hitbox[0]+ mob.hitbox[2]:
    #         self.player.hit(screen)

    # for bullet in bullets:
    #   if bullet.y < mob.hitbox[1] + mob.hitbox[3] and bullet.y > mob.hitbox[1]:
    #     if bullet.x > mob.hitbox[0] and bullet.x < mob.hitbox[0]+ mob.hitbox[2]:
    #       mob.hit()
    #       bullets.pop(bullets.index(bullet))  

    #   if bullet.x < SCREEN_WIDTH and bullet.x > 0:
    #     bullet.x += bullet.speed
    #   else:
    #     bullets.pop(bullets.index(bullet)) 

    # if shootLoop > 0:
    #   shootLoop += 1
    # if shootLoop > 3:
    #   shootLoop = 0

  def Render(self, screen):
    bg = pygame.image.load('assets/bg.jpg')
    bg = pygame.transform.scale(bg, (900, 600))
    screen.blit(bg, (0,0))

    font = pygame.font.SysFont('comicsans', 27, True)
    self.player.draw(screen)
    self.hp.drawHp(screen, self.player)
    text = font.render('HP', 1, (0,0,0))
    screen.blit(text, (0,5))
    self.sp.drawSp(screen, self.player)
    text = font.render('SP', 1, (0,0,0))
    screen.blit(text, (0,30))
    # text = font.render('Score: ' + str(self.score), 1, (255,255,255))
    # screen.blit(text, (690,10))

    for mob in self.mobs:
      mob.draw(screen)

    for bullet in self.bullets:
      bullet.draw(screen)

    pygame.display.update()
