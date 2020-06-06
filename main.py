import pygame
import math
import random
from components.game import Game

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Ragnarok Mob Bashing")
clock = pygame.time.Clock()

# Maps
home_background_image = pygame.image.load('assets/prontera.jpg')

payon_map_1 = pygame.image.load('assets/maps/payon/payon1.jpg')
payon_map_1 = pygame.transform.scale(payon_map_1, (1300, 800)) #payon1
payon_map_1_position = (0, -150)
payon_map_2 = pygame.image.load('assets/maps/payon/payon2.jpg')
payon_map_2 = pygame.transform.scale(payon_map_2, (1100, 800)) #payon2
payon_map_2_position = (-50, -200)
payon_map_3 = pygame.image.load('assets/maps/payon/payon3.jpg')
payon_map_3 = pygame.transform.scale(payon_map_3, (1200, 600)) #payon3
payon_map_3_position = (0, 0)

morroc_map_1 = pygame.image.load('assets/maps/morroc/morroc1.jpg')
morroc_map_1 = pygame.transform.scale(morroc_map_1, (1000, 700)) #morroc1
morroc_map_1_position = (0, -200)
morroc_map_2 = pygame.image.load('assets/maps/morroc/morroc2.jpg')
morroc_map_2 = pygame.transform.scale(morroc_map_2, (1200, 800)) #morroc2
morroc_map_2_position = (0, -200)
morroc_map_3 = pygame.image.load('assets/maps/morroc/morroc3.jpg')
morroc_map_3 = pygame.transform.scale(morroc_map_3, (1200, 700)) #morroc3
morroc_map_3_position = (0, -100)

geffen_map_1 = pygame.image.load('assets/maps/geffen/geffen1.jpg')
geffen_map_1 = pygame.transform.scale(geffen_map_1, (1200, 800)) #geffen1 - culvert
geffen_map_1_position = (0, -300)
geffen_map_2 = pygame.image.load('assets/maps/geffen/geffen2.jpg')
geffen_map_2 = pygame.transform.scale(geffen_map_2, (1000, 600)) #geffen2 - orc village
geffen_map_2_position = (0, -100)
geffen_map_3 = pygame.image.load('assets/maps/geffen/geffen3.jpg')
geffen_map_3 = pygame.transform.scale(geffen_map_3, (1000, 600)) #geffen3 - glast heim
geffen_map_3_position = (0, -100)

island_map_1 = pygame.image.load('assets/maps/island/island1.jpg')
island_map_1 = pygame.transform.scale(island_map_1, (800, 500)) #byalan
island_map_1_position = (0, 0)
island_map_2 = pygame.image.load('assets/maps/island/island2.jpg')
island_map_2 = pygame.transform.scale(island_map_2, (900, 650)) #sunken ship
island_map_2_position = (0, -150)
island_map_3 = pygame.image.load('assets/maps/island/island3.jpg')
island_map_3 = pygame.transform.scale(island_map_3, (1000, 600)) #turtle island
island_map_3_position = (-100, -50)

yuno_map_1 = pygame.image.load('assets/maps/yuno/yuno1.jpg')
yuno_map_1 = pygame.transform.scale(yuno_map_1, (1000, 800)) #yuno1
yuno_map_1_position = (0, -50)
yuno_map_2 = pygame.image.load('assets/maps/yuno/yuno2.jpg') #yuno2 - einbech mine
yuno_map_2_position = (-150, -100)
yuno_map_3 = pygame.image.load('assets/maps/yuno/yuno3.jpg')
yuno_map_3 = pygame.transform.scale(yuno_map_3, (1300, 800)) #yuno3 - juperos
yuno_map_3_position = (-150, 0)

veins_map_1 = pygame.image.load('assets/maps/veins/veins1.jpg')
veins_map_1 = pygame.transform.scale(veins_map_1, (1500, 900)) #veins1 - abyss lake
veins_map_1_position = (-300, -270)
veins_map_2 = pygame.image.load('assets/maps/veins/veins2.jpg')
veins_map_2 = pygame.transform.scale(veins_map_2, (1000, 700)) #veins2 - ice cave
veins_map_2_position = (0, -150)
veins_map_3 = pygame.image.load('assets/maps/veins/veins3.jpg')
veins_map_3 = pygame.transform.scale(veins_map_3, (1000, 800)) #veins3 - thor volcano
veins_map_3_position = (-50, -100)

abbeye_map_1 = pygame.image.load('assets/maps/abbeye/abbeye1.jpg') 
abbeye_map_1 = pygame.transform.scale(abbeye_map_1, (800, 600)) #abbeye1 - niflheim
abbeye_map_1_position = (0, -100)
abbeye_map_2 = pygame.image.load('assets/maps/abbeye/abbeye2.jpg') #abbeye2 - nameless
abbeye_map_2 = pygame.transform.scale(abbeye_map_2, (900, 700))
abbeye_map_2_position = (0, -50)
abbeye_map_3 = pygame.image.load('assets/maps/abbeye/abbeye3.jpg') #abbeye3 - odin temple
abbeye_map_3_position = (0, -220)

banner = pygame.image.load('assets/banner.png')
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
banner_rect.y = 30

play_button = pygame.image.load('assets/play.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3)
play_button_rect.y = math.ceil(screen.get_height() / 1.5)

player_avatar = pygame.image.load('assets/avatar.png')
player_avatar = pygame.transform.scale(player_avatar, (50, 50))
player_avatar_rect = player_avatar.get_rect()
player_avatar_rect.x = 10
player_avatar_rect.y = 10

skill_button_fire = pygame.image.load('assets/fire_btn.png')
skill_button_fire = pygame.transform.scale(skill_button_fire, (35, 35))
skill_button_fire_rect = skill_button_fire.get_rect()
skill_button_fire_rect.x = math.ceil(screen.get_width() / 2.5)
skill_button_fire_rect.y = 10

skill_button_light = pygame.image.load('assets/light_btn.png')
skill_button_light = pygame.transform.scale(skill_button_light, (35, 35))
skill_button_light_rect = skill_button_light.get_rect()
skill_button_light_rect.x = math.ceil(screen.get_width() / 2.5) + 50
skill_button_light_rect.y = 10

skill_button_ice = pygame.image.load('assets/storm_btn.png')
skill_button_ice = pygame.transform.scale(skill_button_ice, (35, 35))
skill_button_ice_rect = skill_button_ice.get_rect()
skill_button_ice_rect.x = math.ceil(screen.get_width() / 2.5) + 100
skill_button_ice_rect.y = 10

potion_indicator = pygame.image.load('assets/potion.png')
potion_indicator = pygame.transform.scale(potion_indicator, (42, 42))
potion_indicator_rect = potion_indicator.get_rect()
potion_indicator_rect.x = screen.get_width() - 120
potion_indicator_rect.y = 5

game = Game()
game_is_running = True

while game_is_running:
  clock.tick(24)

  if game.is_playing:
    if not pygame.mixer.music.get_busy():
      pygame.mixer.music.load('assets/sounds/' + game.current_level + str(game.map_index) + '.wav')
      pygame.mixer.music.play()

    if game.current_level == 'payon':
      if game.map_index == 1:
        screen.blit(payon_map_1, payon_map_1_position) #payon1
      elif game.map_index == 2:
        screen.blit(payon_map_2, payon_map_2_position) #payon2 - payon cave
      elif game.map_index == 3:
        screen.blit(payon_map_3, payon_map_3_position) #payon3 - hidden temple

    if game.current_level == 'morroc':
      if game.map_index == 1:
        screen.blit(morroc_map_1, morroc_map_1_position) #morroc1
      elif game.map_index == 2:
        screen.blit(morroc_map_2, morroc_map_2_position) #morroc2 - ant hell
      elif game.map_index == 3:
        screen.blit(morroc_map_3, morroc_map_3_position) #morroc3 - sphinx

    if game.current_level == 'geffen':
      if game.map_index == 1:
        screen.blit(geffen_map_1, geffen_map_1_position) #geffen1 - culvert
      elif game.map_index == 2:
        screen.blit(geffen_map_2, geffen_map_2_position) #geffen2 - orc village
      elif game.map_index == 3:
        screen.blit(geffen_map_3, geffen_map_3_position) #geffen3 - glast heim

    if game.current_level == 'island':
      if game.map_index == 1:
        screen.blit(island_map_1, island_map_1_position) #island1 - byalan
      elif game.map_index == 2:
        screen.blit(island_map_2, island_map_2_position) #island2 - sunken ship
      elif game.map_index == 3:
        screen.blit(island_map_3, island_map_3_position) #island3 - turtle island

    if game.current_level == 'yuno':
      if game.map_index == 1:
        screen.blit(yuno_map_1, yuno_map_1_position) #yuno1
      elif game.map_index == 2:
        screen.blit(yuno_map_2, yuno_map_2_position) #yuno2 - einbech mine
      elif game.map_index ==3:
        screen.blit(yuno_map_3, yuno_map_3_position) #yuno3 - juperos

    if game.current_level == 'veins':
      if game.map_index == 1:
        screen.blit(veins_map_1, veins_map_1_position) #veins1 - abyss lake
      elif game.map_index == 2:
        screen.blit(veins_map_2, veins_map_2_position) #veins2 - ice cave
      elif game.map_index == 3:
        screen.blit(veins_map_3, veins_map_3_position) #veins3 - thor volcano

    if game.current_level == 'abbeye':
      if game.map_index == 1:
        screen.blit(abbeye_map_1, abbeye_map_1_position) #abbeye1 - niflheim
      if game.map_index == 2:
        screen.blit(abbeye_map_2, abbeye_map_2_position) #abbeye2 - nameless abbeye
      if game.map_index == 3:
        screen.blit(abbeye_map_3, abbeye_map_3_position) #abbeye3 - odin temple

    # Skills bar
    shortcuts_font = pygame.font.SysFont('comicsans', 20, True)
    
    screen.blit(skill_button_fire, skill_button_fire_rect)
    skill_fire_text = shortcuts_font.render('(A)', 1, (255,255,255))
    screen.blit(skill_fire_text, (skill_button_fire_rect.x + 10, skill_button_fire_rect.y + 37))

    screen.blit(skill_button_light, skill_button_light_rect)
    skill_light_text = shortcuts_font.render('(Z)', 1, (255,255,255))
    screen.blit(skill_light_text, (skill_button_light_rect.x + 10, skill_button_light_rect.y + 37))

    if game.player_title == 'wizard' or game.player_title == 'high wizard':
      screen.blit(skill_button_ice, skill_button_ice_rect)
      skill_ice_text = shortcuts_font.render('(E)', 1, (255,255,255))
      screen.blit(skill_ice_text, (skill_button_ice_rect.x + 10, skill_button_ice_rect.y + 37))

    # Player infos
    screen.blit(player_avatar, player_avatar_rect)
    exp_font = pygame.font.SysFont('comicsans', 23, True)
    exp_text = exp_font.render('LV.' + str(game.player.level) + '  -  ' + game.player_title, 1, (255,255,255))
    screen.blit(exp_text, (player_avatar_rect.x + 10, player_avatar.get_height() + 15))

    # Potion
    screen.blit(potion_indicator, potion_indicator_rect)
    potion_font = pygame.font.SysFont('comicsans', 30, True)
    potion_text = potion_font.render('x ' + str(game.player_potions), 1, (255,255,255))
    screen.blit(potion_text, (potion_indicator_rect.x + potion_indicator.get_width(), (potion_indicator_rect.y + potion_indicator.get_height() / 2)))
    potion_shortcut_text = shortcuts_font.render('(P)', 1, (255,255,255))
    screen.blit(potion_shortcut_text, (potion_indicator_rect.x + 12, potion_indicator_rect.y + 42))

    game.update(screen)
    
  else:
    if not pygame.mixer.music.get_busy():
      pygame.mixer.music.load('assets/sounds/start.wav')
      pygame.mixer.music.play()
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
        game.player.cast_spell('wind')
      if event.key == pygame.K_e:
        if game.player_title == 'wizard' or game.player_title == 'high wizard':
          game.player.cast_spell('water')
      if event.key == pygame.K_p:
        game.player.heal(random.randint(25, 35))

    elif event.type == pygame.KEYUP:
      game.pressed[event.key] = False
    
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # Check collision between mouse and button
      if play_button_rect.collidepoint(event.pos):
        game.start()