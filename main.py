import pygame
import math
from components.game import Game

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Ragnarok Mob Bashing")
clock = pygame.time.Clock()

# Maps
home_background_image = pygame.image.load('assets/prontera.jpg')
payon_background_image = pygame.image.load('assets/maps/payon.jpg')
payon_background_image = pygame.transform.scale(payon_background_image, (1200, 600))
morroc_background_image = pygame.image.load('assets/maps/morroc.jpg')
morroc_background_image = pygame.transform.scale(morroc_background_image, (1200, 700))
starry_background_image = pygame.image.load('assets/maps/starry.jpg')
starry_background_image = pygame.transform.scale(starry_background_image, (1000, 600))
einbech_background_image = pygame.image.load('assets/maps/einbech.jpg')
abyss_background_image = pygame.image.load('assets/maps/abyss.jpg')
abyss_background_image = pygame.transform.scale(abyss_background_image, (1500, 900))
odin_background_image = pygame.image.load('assets/maps/odin.jpg')

banner = pygame.image.load('assets/banner.png')
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
banner_rect.y = 10

play_button = pygame.image.load('assets/play.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3)
play_button_rect.y = math.ceil(screen.get_height() / 1.5)

game = Game()
game_is_running = True

while game_is_running:
  clock.tick(24)

  if game.is_playing:
    if game.current_level == 'payon':
      screen.blit(payon_background_image, (0, 0))
    if game.current_level == 'morroc':
      screen.blit(morroc_background_image, (0, -100))
    if game.current_level == 'starry':
      screen.blit(starry_background_image, (0, -100))
    if game.current_level == 'einbech':
      screen.blit(einbech_background_image, (-150, -100))
    if game.current_level == 'abyss':
      screen.blit(abyss_background_image, (-300, -270))
    if game.current_level == 'odin':
      screen.blit(odin_background_image, (0, -220))
    game.update(screen)
    
  else:
    screen.blit(home_background_image, (0, -200))
    screen.blit(banner, banner_rect)
    screen.blit(play_button, play_button_rect)

  # Update screen
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_is_running = False
      pygame.quit()

    elif event.type == pygame.KEYDOWN:
      game.pressed[event.key] = True
      if event.key == pygame.K_a:
        game.player.cast_spell('fire')
      if event.key == pygame.K_z:
        game.player.cast_spell('light')

    elif event.type == pygame.KEYUP:
      game.pressed[event.key] = False
    
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # Check collision between mouse and button
      if play_button_rect.collidepoint(event.pos):
        game.start()