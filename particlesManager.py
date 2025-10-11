import random
import particles
from Variables import *

def fill_dico():
    """Remplit le dictionnaire des particules avec du vide."""
    for x in range(0, draw_area_width, blockSize):
        for y in range(0, height, blockSize):
            particlesDict[(x, y)] = particles.Empty


def put_particle(pos, particleType):
    """Place une particule à une position donnée."""
    x, y = pos
    # Aligne sur la grille
    x = (x // blockSize) * blockSize
    y = (y // blockSize) * blockSize
    # Vérifie les limites
    if not (0 <= x < draw_area_width and 0 <= y < height):
        return
    particle_rect = pygame.Rect(x, y, blockSize, blockSize)
    pygame.draw.rect(grid_surface, particleType.color, particle_rect)
    particlesDict[(x, y)] = particleType


def move_particle(old_pos, new_pos):
    """Déplace une particule d'une position à une autre."""
    # Ne sort jamais des limites de la zone de dessin
    if not (0 <= new_pos[0] < draw_area_width and 0 <= new_pos[1] < height):
        return

    particle = particlesDict.get(old_pos, particles.Empty)
    if particle == particles.Empty:
        return

    # Efface ancienne position
    pygame.draw.rect(grid_surface, (0, 0, 0), pygame.Rect(old_pos[0], old_pos[1], blockSize, blockSize))
    particlesDict[old_pos] = particles.Empty

    # Dessine à la nouvelle position
    pygame.draw.rect(grid_surface, particle.color, pygame.Rect(new_pos[0], new_pos[1], blockSize, blockSize))
    particlesDict[new_pos] = particle


def updateAllParticles(canvasSize, blockSize):
    """Met à jour toutes les particules à chaque frame."""
    # Itération du bas vers le haut (pour éviter les "téléportations")
    for v in range(canvasSize[1] - blockSize, -1, -blockSize):
        for u in range(0, draw_area_width, blockSize):
            if (u, v) not in particlesDict:
                continue
            particle = particlesDict[(u, v)]
            if particle == particles.Empty:
                continue

            # --- Gestion spéciale des liquides ---
            if particle in [particles.Water, particles.Lava]:
                below = (u, v + blockSize)
                left = (u - blockSize, v)
                right = (u + blockSize, v)
                below_left = (u - blockSize, v + blockSize)
                below_right = (u + blockSize, v + blockSize)

                # Descente directe si vide
                if below in particlesDict and particlesDict[below] == particles.Empty:
                    move_particle((u, v), below)

                # Sinon diagonale gauche/droite aléatoire
                elif random.choice([True, False]):
                    if below_left in particlesDict and particlesDict[below_left] == particles.Empty:
                        move_particle((u, v), below_left)
                    elif below_right in particlesDict and particlesDict[below_right] == particles.Empty:
                        move_particle((u, v), below_right)
                    elif left in particlesDict and particlesDict[left] == particles.Empty:
                        move_particle((u, v), left)
                    elif right in particlesDict and particlesDict[right] == particles.Empty:
                        move_particle((u, v), right)
                else:
                    if below_right in particlesDict and particlesDict[below_right] == particles.Empty:
                        move_particle((u, v), below_right)
                    elif below_left in particlesDict and particlesDict[below_left] == particles.Empty:
                        move_particle((u, v), below_left)
                    elif right in particlesDict and particlesDict[right] == particles.Empty:
                        move_particle((u, v), right)
                    elif left in particlesDict and particlesDict[left] == particles.Empty:
                        move_particle((u, v), left)

            # --- Gestion normale des solides et autres particules ---
            else:
                getRulesOfParticle(particle, (u, v))


def getRulesOfParticle(particle, coords):
    """Applique les règles de comportement d'une particule solide."""
    coords = (coords[0] // blockSize * blockSize, coords[1] // blockSize * blockSize)
    rules = particle.rules
    if not rules:
        return
    successRule = None
    for rule in rules:
        # Vérifie les conditions de la règle
        conditions = []
        posOfCondition = []
        for c in range(1, 9):
            if rule[c] != "F":
                conditions.append(int(rule[c]))
                posOfCondition.append(c)

        rule_success = True
        for i in range(len(conditions)):
            match conditions[i]:
                case 0: wantedClass = particles.Empty
                case 1: wantedClass = particles.Sand
                case 2: wantedClass = particles.Rock
                case 3: wantedClass = particles.Steel
                case 4: wantedClass = particles.Water
                case 5: wantedClass = particles.Lava
                case 6: wantedClass = particles.Glass
                case _: wantedClass = particles.Empty

            # Index clockwise
            match posOfCondition[i]:
                case 1: posOffset = (0, -blockSize)
                case 2: posOffset = (blockSize, -blockSize)
                case 3: posOffset = (blockSize, 0)
                case 4: posOffset = (blockSize, blockSize)
                case 5: posOffset = (0, blockSize)
                case 6: posOffset = (-blockSize, blockSize)
                case 7: posOffset = (-blockSize, 0)
                case 8: posOffset = (-blockSize, -blockSize)
                case _: posOffset = (0, 0)

            neighbor_coords = (coords[0] + posOffset[0], coords[1] + posOffset[1])
            neighbor = particlesDict.get(neighbor_coords, particles.Empty)
            if neighbor != wantedClass:
                rule_success = False
                break

        if rule_success:
            successRule = rule
            break

    if not successRule:
        return

    rule = successRule
    val = int(rule[9])
    match val:
        case 1: tileToCreate = particles.Sand
        case 2: tileToCreate = particles.Rock
        case 3: tileToCreate = particles.Steel
        case 4: tileToCreate = particles.Water
        case 5: tileToCreate = particles.Lava
        case 6: tileToCreate = particles.Glass
        case _: tileToCreate = particles.Empty

    # --- Vérifie d'abord que la règle a une destination valide ---
    valid_move = False
    valid_targets = []
    for r in range(10, 18):
        if int(rule[r]) != 0:
            destinationIndex = r - 9
            match destinationIndex:
                case 1: posOffset = (0, -blockSize)
                case 2: posOffset = (blockSize, -blockSize)
                case 3: posOffset = (blockSize, 0)
                case 4: posOffset = (blockSize, blockSize)
                case 5: posOffset = (0, blockSize)
                case 6: posOffset = (-blockSize, blockSize)
                case 7: posOffset = (-blockSize, 0)
                case 8: posOffset = (-blockSize, -blockSize)
                case _: posOffset = (0, 0)

            target_pos = (coords[0] + posOffset[0], coords[1] + posOffset[1])
            if 0 <= target_pos[0] < draw_area_width and 0 <= target_pos[1] < height:
                valid_move = True
                valid_targets.append(target_pos)

    if not valid_move:
        return

    # Supprime ancienne particule seulement si un mouvement est possible
    particlesDict[(coords[0], coords[1])] = particles.Empty
    pygame.draw.rect(grid_surface, (0, 0, 0), pygame.Rect(coords[0], coords[1], blockSize, blockSize))

    # Applique les destinations valides
    for target_pos in valid_targets:
        if 0 <= target_pos[0] < draw_area_width and 0 <= target_pos[1] < height:
            put_particle(target_pos, tileToCreate)


def clearParticles(canvasSize):
    """Vide complètement la grille."""
    for u in range(0, draw_area_width, blockSize):
        for v in range(0, canvasSize[1], blockSize):
            particlesDict[(u, v)] = particles.Empty
