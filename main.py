import particlesManager
import pygame
pygame.init()
def window():
  width, height = 1400, 800
  screen = pygame.display.set_mode((width, height))
  blocksize = 2
  pygame.display.set_caption("Sand_simulation")
  clock = pygame.time.Clock()
  running = True
  while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
