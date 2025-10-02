class Empty():
	index = 0
	rules = []
	color = (255,255,255)
	speed = 0 #Vitesse de dessente sur la grille

class Sand():
	index = 1
	rules = ["1FFFF0FFF100001000","1FFF0FFFF100010000","1FFFFF1FF100000100"]
	color = (237,237,26)
	speed = 2

class Rock():
	index = 2
	rules = ["2FFFF0FFF200001000"]
	color = (95,95,95)
	speed = 3

class Steel():
	index = 3
	rules = ["3FFFFFFFFF30000000"]
	color = (192,192,192)
	speed = 0

class Water():
	index = 4
	rules = ["4FFFF0FFF400004000","4FFF0FFFF400040000","4FFFFF0FF400000400"]
	color = (76, 124, 234)
	speed = 2

class Lava():
	index = 5
	rules = ["5"]
	color = (213, 76, 2)
	speed = 1

class Glass():
	index = 6
	rules = ["6"]
	color = (240,240,240)
	speed = 0
