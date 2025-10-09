from Variables import *
import particlesManager
from particles import *
import pygame
import math

pygame.init()


# Différents imports + initiation de pygame
def window():
    pygame.display.set_caption("Sand_simulation")
    clock = pygame.time.Clock()
    brush_size = 3  # taille de base du pinceau (en nombre de blocs)

    toggleGrid = True
    hasGrid = False

    # Dessin de la grille
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(grid_surface, (0, 0))

        if toggleGrid:
            toggleGrid = False
            hasGrid = not hasGrid
            if (hasGrid):
                for x in range(0, draw_area_width, blocksize):
                    pygame.draw.line(grid_surface, (255, 255, 255), (x, 0), (x, height))
                for y in range(0, height, blocksize):
                    pygame.draw.line(grid_surface, (255, 255, 255), (0, y), (draw_area_width, y))
            else:
                for x in range(0, draw_area_width, blocksize):
                    pygame.draw.line(grid_surface, (0, 0, 0), (x, 0), (x, height))
                for y in range(0, height, blocksize):
                    pygame.draw.line(grid_surface, (0, 0, 0), (0, y), (draw_area_width, y))

        palette = pygame.Rect(width - 150, 0, 150, height)
        pygame.draw.rect(screen, (0, 0, 0), palette, 0)
        pygame.draw.circle(screen, Water.color, (Water.x, Water.y), circle_radius)
        pygame.draw.circle(screen, Sand.color, (Sand.x, Sand.y), circle_radius)
        pygame.draw.circle(screen, Lava.color, (Lava.x, Lava.y), circle_radius)
        pygame.draw.circle(screen, Rock.color, (Rock.x, Rock.y), circle_radius)
        pygame.draw.circle(screen, Steel.color, (Steel.x, Steel.y), circle_radius)
        pygame.draw.circle(screen, Glass.color, (Glass.x, Glass.y), circle_radius)
        # choisir la matière
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # permet de quitter la fenêtre
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos

                    # clique sur la palette
                    if math.dist((mouse_x, mouse_y), (Sand.x, Sand.y)) <= circle_radius:
                        Sand.is_used = True
                        Water.is_used = Lava.is_used = Rock.is_used = Steel.is_used = Glass.is_used = False
                    elif math.dist((mouse_x, mouse_y), (Water.x, Water.y)) <= circle_radius:
                        Water.is_used = True
                        Sand.is_used = Lava.is_used = Rock.is_used = Steel.is_used = Glass.is_used = False
                    elif math.dist((mouse_x, mouse_y), (Lava.x, Lava.y)) <= circle_radius:
                        Lava.is_used = True
                        Water.is_used = Sand.is_used = Rock.is_used = Steel.is_used = Glass.is_used = False
                    elif math.dist((mouse_x, mouse_y), (Rock.x, Rock.y)) <= circle_radius:
                        Rock.is_used = True
                        Water.is_used = Lava.is_used = Sand.is_used = Steel.is_used = Glass.is_used = False
                    elif math.dist((mouse_x, mouse_y), (Steel.x, Steel.y)) <= circle_radius:
                        Steel.is_used = True
                        Water.is_used = Lava.is_used = Rock.is_used = Sand.is_used = Glass.is_used = False
                    elif math.dist((mouse_x, mouse_y), (Glass.x, Glass.y)) <= circle_radius:
                        Glass.is_used = True
                        Water.is_used = Lava.is_used = Rock.is_used = Steel.is_used = Sand.is_used = False
            elif event.type == pygame.KEYDOWN:
                # --- Changement de taille du pinceau ---
                if event.key == pygame.K_1:
                    brush_size = 1
                elif event.key == pygame.K_2:
                    brush_size = 2
                elif event.key == pygame.K_3:
                    brush_size = 3
                elif event.key == pygame.K_4:
                    brush_size = 4
                elif event.key == pygame.K_5:
                    brush_size = 5
                elif event.key == pygame.K_g:
                    toggleGrid = not toggleGrid
        if pygame.mouse.get_pressed()[0]:
            if Sand.is_used:
                particlesManager.put_particle(brush_size, Sand)
            if Water.is_used:
                particlesManager.put_particle(brush_size, Water)
            if Lava.is_used:
                particlesManager.put_particle(brush_size, Lava)
            if Steel.is_used:
                particlesManager.put_particle(brush_size, Steel)
            if Rock.is_used:
                particlesManager.put_particle(brush_size, Rock)
            if Glass.is_used:
                particlesManager.put_particle(brush_size, Glass)

        for (row, col), particleType in particles.items():
            rect = pygame.Rect(col * blocksize,
                               row * blocksize,
                               blocksize, blocksize)
            pygame.draw.rect(grid_surface, particleType.color, rect)
        screen.blit(grid_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
window()


