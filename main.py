import pygame
from player import Player
from fireball import Fireball
from monster import Monster
from bar import Bar

SCREEN_WIDTH = 800

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH,500))
pygame.display.set_caption("Ragnarok Online")
clock = pygame.time.Clock()

bg = pygame.image.load('assets/bg.jpg')

music = pygame.mixer.music.load('sounds/prontera.mp3')
pygame.mixer.music.play(-1) # -1 will ensure the song keeps looping
pygame.mixer.music.set_volume(0.1)

fireballSound = pygame.mixer.Sound('sounds/fireball.wav')


def redrawGameWindow():
  window.blit(bg, (0,0))
  player.draw(window)
  mob.draw(window)
  hp.drawHp(window, player)
  text = font.render('HP', 1, (0,0,0))
  window.blit(text, (0,5))
  sp.drawSp(window, player)
  text = font.render('SP', 1, (0,0,0))
  window.blit(text, (0,30))

  for bullet in bullets:
    bullet.draw(window)
  pygame.display.update()

# Main loop
font = pygame.font.SysFont('comicsans', 27, True)
run = True
player = Player(300, 300, 64, 64)
mob = Monster(200, 310, 64, 64, 500)
hp = Bar(30, 5, 200, 20)
sp = Bar(30, 30, 200, 20)
bullets = []
shootLoop = 0
facing = -1

while run:
  clock.tick(24)

  PLAYER_REGEN_SP = pygame.USEREVENT + 1

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    elif event.type == PLAYER_REGEN_SP:
      if player.sp < 100 and player.sp < sp.width:
        player.sp += 10  

  if mob.visible == True:
    if player.hitbox[1] < mob.hitbox[1] + mob.hitbox[3] and player.hitbox[1] + player.hitbox[3] > mob.hitbox[1]:
      if player.hitbox[0] + player.hitbox[2] > mob.hitbox[0] and player.hitbox[0] < mob.hitbox[0]+ mob.hitbox[2]:
        player.hit(window)

  for bullet in bullets:
    if bullet.y < mob.hitbox[1] + mob.hitbox[3] and bullet.y > mob.hitbox[1]:
      if bullet.x > mob.hitbox[0] and bullet.x < mob.hitbox[0]+ mob.hitbox[2]:
        mob.hit()
        bullets.pop(bullets.index(bullet))  

    if bullet.x < SCREEN_WIDTH and bullet.x > 0:
      bullet.x += bullet.speed
    else:
      bullets.pop(bullets.index(bullet)) 

  if shootLoop > 0:
    shootLoop += 1
  if shootLoop > 3:
    shootLoop = 0

  keys = pygame.key.get_pressed()

  if not (player.dead):
    if keys[pygame.K_SPACE] and shootLoop == 0:
      player.hitting = False
      if player.sp > 0:
        fireballSound.play()
        fireball = Fireball(round(player.x + player.width//2), round(player.y + player.height//2), facing)
        player.sp -= 15
        if len(bullets) < 5:
          bullets.append(fireball)
        shootLoop = 1

    if keys[pygame.K_LEFT] and player.x > player.speed:
      pygame.time.set_timer(PLAYER_REGEN_SP, 0)
      player.hitting = False
      player.x -= player.speed
      player.left = True
      player.right = False
      player.standing = False
      player.isSitting = False
      facing = -1
    elif keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.width - player.speed:
      pygame.time.set_timer(PLAYER_REGEN_SP, 0)
      player.hitting = False
      player.x += player.speed
      player.left = False
      player.right = True
      player.standing = False
      player.isSitting = False
      facing = 1
    else:
      player.standing = True
      player.walkCount = 0
    
    if not (player.isJumping):
      if keys[pygame.K_UP]:
        player.hitting = False
        player.isJumping = True
        player.right = False
        player.left = False
        player.walkCount = 0
        player.isSitting = False
      elif keys[pygame.K_DOWN]:
        pygame.time.set_timer(PLAYER_REGEN_SP, 1000)
        player.hitting = False
        player.isJumping = False
        player.right = False
        player.left = False
        player.isSitting = True
        player.walkCount = 0
    else:
      if player.jumpCount >= -10:
        neg = 1
        if player.jumpCount < 0:
          neg = -1
        player.y -= (player.jumpCount ** 2) * 0.5 * neg
        player.jumpCount -= 1
      else:
        player.isJumping = False
        player.jumpCount = 10

  redrawGameWindow()
  
pygame.quit()
