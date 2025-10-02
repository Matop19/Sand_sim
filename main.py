from Variables import *
import particlesManager
import particles
import pygame
pygame.init()
#Différents imports + initiation de pygame

def window():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sand_simulation")
    clock = pygame.time.Clock()
    #initier la page

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    #permet de quitter la fenêtre

        screen.fill((225,225,225))
        for row in range(0,width):
            for col in range(0,height):
                rect = pygame.Rect(col * blocksize,
                                   row * blocksize,
                                   blocksize, blocksize)
                pygame.draw.rect(screen, (0,0,0), rect, 1)
        #Création de la grille

        palette = pygame.Rect(width-200, 0, 200, height)
        pygame.draw.rect(screen, (0,0,0), palette, 0)
        pygame.draw.circle(screen, particles.Water.color, (particles.Water.x,particles.Water.y), circle_radius)
        pygame.draw.circle(screen, particles.Sand.color, (particles.Sand.x, particles.Sand.y), circle_radius)
        pygame.draw.circle(screen, particles.Lava.color, (particles.Lava.x, particles.Lava.y), circle_radius)
        pygame.draw.circle(screen, particles.Rock.color, (particles.Rock.x, particles.Rock.y), circle_radius)
        pygame.draw.circle(screen, particles.Steel.color, (particles.Steel.x, particles.Steel.y), circle_radius)
        pygame.draw.circle(screen, particles.Glass.color, (particles.Glass.x, particles.Glass.y), circle_radius)
        #choisir la matière

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
window()
