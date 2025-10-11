from Variables import *
class Empty():
    index = 0
    rules = []
    color = (255,255,255)
    speed = 0 #Vitesse de dessente sur la grille (plus le chiffre est petit, plus c'est lent)

class Sand():
    index = 1
    rules = ["1FFFF0FFF100001000","1FFF0FFFF100010000","1FFFFF0FF100000100"]
    color = (237,237,26)
    speed = 2
    is_used = False
    x, y = width - 100, 50

class Rock():
    index = 2
    rules = ["2FFFF0FFF200001000"]
    color = (95,95,95)
    speed = 3
    is_used = False
    x, y = width - 50, 50

class Steel():
    index = 3
    rules = []
    color = (192,192,192)
    speed = 0
    is_used = False
    x, y = width - 100, 125

class Water():
    index = 4from Variables import *
class Empty():
    index = 0
    rules = []
    color = (255,255,255)
    speed = 0 #Vitesse de dessente sur la grille (plus le chiffre est petit, plus c'est lent)

class Sand():
    index = 1
    rules = ["1FFFF0FFF100001000","1FFFF4FFF100001000","1FFFF5FFF100001000","1FFF0FFFF100010000","1FFFFF0FF100000100"]
    color = (237,237,26)
    speed = 2
    is_used = False
    x, y = width - 100, 50

class Rock():
    index = 2
    rules = ["2FFFF0FFF200001000","2FFFF4FFF200001000","2FFFF5FFF200001000"]
    color = (95,95,95)
    speed = 3
    is_used = False
    x, y = width - 50, 50

class Steel():
    index = 3
    rules = []
    color = (192,192,192)
    speed = 0
    is_used = False
    x, y = width - 100, 125

class Water():
    index = 4
    rules = [
        # Descente directe si vide dessous
        "4FFFF0FFF400001000",  
        # Descente diagonale gauche si bas bloqué mais bas-gauche vide
        "4FFFFF0FF400010000",
        # Descente diagonale droite si bas bloqué mais bas-droite vide
        "4FF0FFFFF400100000",
        # Glisse à gauche si bloqué partout en bas mais vide à gauche
        "4FFFFFF0F400000010",
        # Glisse à droite si bloqué partout en bas mais vide à droite
        "4FFFF0FFF400000100"
    ]
    color = (76, 124, 234)
    speed = 2
    is_used = False
    x, y = width - 50, 125

class Lava():
    index = 5
    rules = [
        # Descente directe si vide dessous
        "5FFFF0FFF500001000",
        # Descente diagonale gauche si bas bloqué mais bas-gauche vide
        "5FFFFF0FF500010000",
        # Descente diagonale droite si bas bloqué mais bas-droite vide
        "5FF0FFFFF500100000",
        # Glisse à gauche si bloquée partout en bas mais vide à gauche
        "5FFFFFF0F500000010",
        # Glisse à droite si bloquée partout en bas mais vide à droite
        "5FFFF0FFF500000100"
    ]
    color = (213, 76, 2)
    speed = 1
    is_used = False
    x, y = width - 100, 200

class Glass():
    index = 6
    rules = []
    color = (240,240,240)
    speed = 0
    is_used = False
    x, y = width - 50, 200
    rules = ["4FFFF0FFF400001000","4FFF0FFFF400010000","4FFFFF0FF400000100","4FFFFF0FF400000010","4FF0FFFFF400100000"]
    color = (76, 124, 234)
    speed = 2
    is_used = False
    x, y = width - 50, 125

class Lava():
    index = 5
    rules = ["5FFFF0FFF500001000","5FFF0FFFF500010000","5FFFFF0FF500000100","5FFFFF0FF500000010","5FF0FFFFF500100000"]
    color = (213, 76, 2)
    speed = 1
    is_used = False
    x, y = width - 100, 200

class Glass():
    index = 6
    rules = []
    color = (240,240,240)
    speed = 0
    is_used = False
    x, y = width - 50, 200
