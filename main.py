import pygame
import math
from components.game import Game

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Ragnarok Online")
clock = pygame.time.Clock()

home_background_image = pygame.image.load('assets/prontera.jpg')
play_background_image = pygame.image.load('assets/bg.jpg')

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
    screen.blit(play_background_image, (0, 0))
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