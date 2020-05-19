import pygame
import random
from components.game import Game

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Ragnarok Online")
clock = pygame.time.Clock()
background_image = pygame.image.load('assets/bg.jpg')

game = Game()
game_is_running = True

while game_is_running:
  clock.tick(24)
  screen.blit(background_image, (0, 0))
  game.update(screen)
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
      if event.key == pygame.K_SPACE:
        game.start()

    elif event.type == pygame.KEYUP:
      game.pressed[event.key] = False
    