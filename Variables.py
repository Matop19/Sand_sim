import pygame
width, height = 1050, 600
circle_radius = 12.5
blockSize = 5
particlesDict = {}
screen = pygame.display.set_mode((width, height))
draw_area_width = width - 150  # largeur réelle de la grille
grid_surface = pygame.Surface((draw_area_width, height))
