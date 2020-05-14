import pygame
from scenes.base import SceneBase
from scenes.base import GameScene

class TitleScene(SceneBase):
  def __init__(self):
    SceneBase.__init__(self)
  
  def ProcessInput(self, events, pressed_keys):
    for event in events:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        # Move to the next scene when the user pressed Enter
        self.SwitchToScene(GameScene())

  def Update(self):
    pass

  def Render(self, screen):
    bg = pygame.image.load('assets/ro_bg.jpg')
    bg = pygame.transform.scale(bg, (900, 600))
    screen.blit(bg, (0,0))

    font = pygame.font.SysFont('comicsans', 50, True)
    text = font.render('PRESS ENTER', 1, (0,0,0))
    screen.blit(text, (300,300))