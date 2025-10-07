import particles
from Variables import *
def put_particle(brush_size, particleType):
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
				pygame.draw.rect(grid_surface, particleType.color, sand_rect)
