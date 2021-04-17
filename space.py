#! /usr/bin/env python3
from Planet import *
import OrbitalFunctions
import Universe

import numpy as np
import pygame
from pygame.locals import *

p = Planet(1., 0.)
p.radius = 40
p.set_pos(500, 140)
p.v[0] = -100
p.v[1] = 0
p.x[0] = 500
p.x[1] = 140
p.surface_gravity = 7
p.set_color(0, 0, 255)
p.name = "walnut"

p2 = Planet(100., 0.)
p2.radius = 30
p2.set_pos(600, 500)
p2.v[0] = -100
p2.v[1] = -100
p2.x[0] = 600
p2.x[1] = 500
p2.surface_gravity = 10
p2.set_color(0, 255, 0)
p2.name = "bruh"

all_planets = [p, p2]

#--------------#
# pygame stuff #
#--------------#

pygame.init()
pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 12)

window = (1280, 720)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

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

    for planet in all_planets:
        planet.update_velocity(all_planets, Universe.TIME_STEP)
        print("{}'s vel =\t[{:.3f}, {:.3f}]".format(
            planet.name, planet.v[0], planet.v[1]))
        planet.update_position(Universe.TIME_STEP)
        pygame.draw.circle(screen, planet.get_color(), planet.get_pos(), planet.get_radius())
        text = font_renderer.render(planet.name, True, (0, 0, 0))
        screen.blit(text, planet.get_pos())
    # flip the display
    pygame.display.flip()

pygame.quit()
