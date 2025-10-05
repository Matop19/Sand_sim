import particles
from Variables import *
def put_sand_particles(brush_size):
    if particles.Sand.is_used and pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= width - 150:
            return
        grid_x = mouse_x // blocksize
        grid_y = mouse_y // blocksize
        for dx in range(-brush_size + 1, brush_size):
            for dy in range(-brush_size + 1, brush_size):
                x = (grid_x + dx) * blocksize
                y = (grid_y + dy) * blocksize
                if 0 <= x < width - 150 and 0 <= y < height:
                    sand_rect = pygame.Rect(x, y, blocksize, blocksize)
                    pygame.draw.rect(grid_surface, particles.Sand.color, sand_rect)
def put_water_particles(brush_size):
    if particles.Water.is_used and pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= width - 150:
            return
        grid_x = mouse_x // blocksize
        grid_y = mouse_y // blocksize
        for dx in range(-brush_size + 1, brush_size):
            for dy in range(-brush_size + 1, brush_size):
                x = (grid_x + dx) * blocksize
                y = (grid_y + dy) * blocksize
                if 0 <= x < width - 150 and 0 <= y < height:
                    water_rect = pygame.Rect(x, y, blocksize, blocksize)
                    pygame.draw.rect(grid_surface, particles.Water.color, water_rect)
def put_lava_particles(brush_size):
    if particles.Lava.is_used and pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= width - 150:
            return
        grid_x = mouse_x // blocksize
        grid_y = mouse_y // blocksize
        for dx in range(-brush_size + 1, brush_size):
            for dy in range(-brush_size + 1, brush_size):
                x = (grid_x + dx) * blocksize
                y = (grid_y + dy) * blocksize
                if 0 <= x < width - 150 and 0 <= y < height:
                    lava_rect = pygame.Rect(x, y, blocksize, blocksize)
                    pygame.draw.rect(grid_surface, particles.Lava.color, lava_rect)
def put_steel_particles(brush_size):
    if particles.Steel.is_used and pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= width - 150:
            return
        grid_x = mouse_x // blocksize
        grid_y = mouse_y // blocksize
        for dx in range(-brush_size + 1, brush_size):
            for dy in range(-brush_size + 1, brush_size):
                x = (grid_x + dx) * blocksize
                y = (grid_y + dy) * blocksize
                if 0 <= x < width - 150 and 0 <= y < height:
                    steel_rect = pygame.Rect(x, y, blocksize, blocksize)
                    pygame.draw.rect(grid_surface, particles.Steel.color, steel_rect)
def put_rock_particles(brush_size):
    if particles.Rock.is_used and pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= width - 150:
            return
        grid_x = mouse_x // blocksize
        grid_y = mouse_y // blocksize
        for dx in range(-brush_size + 1, brush_size):
            for dy in range(-brush_size + 1, brush_size):
                x = (grid_x + dx) * blocksize
                y = (grid_y + dy) * blocksize
                if 0 <= x < width - 150 and 0 <= y < height:
                    rock_rect = pygame.Rect(x, y, blocksize, blocksize)
                    pygame.draw.rect(grid_surface, particles.Rock.color, rock_rect)
def put_glass_particles(brush_size):
    if particles.Glass.is_used and pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= width - 150:
            return
        grid_x = mouse_x // blocksize
        grid_y = mouse_y // blocksize
        for dx in range(-brush_size + 1, brush_size):
            for dy in range(-brush_size + 1, brush_size):
                x = (grid_x + dx) * blocksize
                y = (grid_y + dy) * blocksize
                if 0 <= x < width - 150 and 0 <= y < height:
                    glass_rect = pygame.Rect(x, y, blocksize, blocksize)
                    pygame.draw.rect(grid_surface, particles.Glass.color, glass_rect)
