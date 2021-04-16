#! /usr/bin/env python3
from Planet import *
import OrbitalFunctions
import Universe

import numpy as np
import pygame
from pygame.locals import *

p = Planet(0., 0.)
p.radius = 40
p.x[0] = 150
p.x[1] = 140
p.set_color(0, 0, 255)

p2 = Planet(0., 0.)
p.radius = 30
p.x[0] = 30
p.x[1] = 500
p.set_color(0, 255, 0)

all_planets = [p, p2]

#--------------#
# pygame stuff #
#--------------#

pygame.init()

screen = pygame.display.set_mode([1280, 720])

running = True
while running:

    # check if user closed game
    for event in pygame.event.get():
        if event.type == QUIT:
            print("quitting game...")
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # while background
    screen.fill((255, 255, 255))

    # draw solid blue circle in center
    pygame.draw.circle(screen, p.get_color(), p.get_pos(), p.get_radius())

    p.update_velocity(all_planets, Universe.TIME_STEP)
    for planet in all_planets:
        planet.update_position(Universe.TIME_STEP)

#    x, y = p.get_pos()
#    p.set_pos(x + 1, y)
#
#    if x > 1_000:
#        p.set_pos(0, y)

    # flip the display
    pygame.display.flip()

pygame.quit()
