import particlesManager
import pygame
pygame.init()
def window():
    width, height = 1400, 800
    screen = pygame.display.set_mode((width, height))
    blocksize = 10
    pygame.display.set_caption("Sand_simulation")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((225,225,225))
        for row in range(0,width):
            for col in range(0,height):
                rect = pygame.Rect(col * blocksize,
                                   row * blocksize,
                                   blocksize, blocksize)
                pygame.draw.rect(screen, (0,0,0), rect, 1)
        picker = pygame.Rect(width-200, 0, 200, height)
        pygame.draw.rect(screen, (0,0,0), picker, 0)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
window()

