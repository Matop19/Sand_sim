import pygame
import particles
from Variables import *


def put_particle(pos, particleType):
    particle_rect = pygame.Rect(pos[0], pos[1], blockSize, blockSize)
    pygame.draw.rect(grid_surface, particleType.color, particle_rect)
    particlesDict[(pos[0], pos[1])] = particleType


def getRulesOfParticle(particle, coords):
    rules = particle.rules
    successRule = None

    for rule in rules:
        # --- Vérifie les conditions ---
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

            # --- Index clockwise (1 = haut milieu) ---
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

    # --- Pas de règle applicable ---
    if not successRule:
        return

    rule = successRule

    # --- Type de tuile à créer = 10e caractère ---
    val = int(rule[9])
    match val:
        case 1: tileToCreate = particles.Sand
        case 2: tileToCreate = particles.Rock
        case 3: tileToCreate = particles.Steel
        case 4: tileToCreate = particles.Water
        case 5: tileToCreate = particles.Lava
        case 6: tileToCreate = particles.Glass
        case _: tileToCreate = particles.Empty

    # --- Supprime la particule originale ---
    particlesDict[(coords[0], coords[1])] = particles.Empty
    pygame.draw.rect(grid_surface, (0, 0, 0), pygame.Rect(coords[0], coords[1], blockSize, blockSize))

    # --- Applique les destinations (positions 10 à 17 incluses) ---
    for r in range(10, 18):
        if int(rule[r]) != 0:  # destination active
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
            put_particle(target_pos, tileToCreate)


def updateAllParticles(canvasSize, blockSize):
    # Itération du bas vers le haut
    for v in range(canvasSize[1] - blockSize, -1, -blockSize):
        for u in range(0, canvasSize[0], blockSize):
            if (u, v) in particlesDict:
                particle = particlesDict[(u, v)]
                if particle != particles.Empty:
                    getRulesOfParticle(particle, (u, v))


def clearParticles(canvasSize):
    for u in range(0, canvasSize[0], blockSize):
        for v in range(0, canvasSize[1], blockSize):
            particlesDict[(u, v)] = particles.Empty
