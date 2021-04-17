#! /usr/bin/env python3
from Planet import *
import OrbitalFunctions
import Universe

import numpy as np
import pygame
from pygame.locals import *

# temp1 = Planet(1.0, 0.0)
# temp1.radius = 40
# temp1.set_pos(100, 250)
# temp1.v[0] = 100
# temp1.v[1] = 0
# temp1.surface_gravity = 200
# temp1.set_color(0, 0, 255)
# temp1.name = "top"

# temp2 = Planet(1.0, 0.0)
# temp2.radius = 40
# temp2.set_pos(100, 500)
# temp2.v[0] = 100
# temp2.v[1] = 0
# temp2.surface_gravity = 200
# temp2.set_color(0, 255, 0)
# temp2.name = "bottom"

p = Planet(1., 0.)
p.radius = 50
p.set_pos(640, 360)
p.v[0] = 0
p.v[1] = 0
p.x[0] = 500
p.x[1] = 140
p.surface_gravity = 7000
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

p3 = Planet(100., 0.)
p3.radius = 50
p3.set_pos(800, 200)
p3.v[0] = -200
p3.v[1] = -200
p3.x[0] = 800
p3.x[1] = 200
p3.surface_gravity = 10
p3.set_color(255, 0, 0)
p3.name = "tucan"

all_planets = [p, p2, p3]

#--------------#
# pygame stuff #
#--------------#

pygame.init()
pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 12)
clock = pygame.time.Clock()

window = (1280, 720)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

running = True
pause = True

while pause:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = False

while running:

    dt = clock.tick(60)

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

    for i in range(len(all_planets)):
        for k in all_planets[i:]:
            pygame.draw.line(screen, (0, 0, 0), all_planets[i].get_pos(), k.get_pos())

    for planet in all_planets:
        planet.update_velocity(all_planets, Universe.TIME_STEP)
        print("{}'s vel =\t[{:.3f}, {:.3f}],\tnormed = {}".format(
            planet.name, planet.v[0], planet.v[1], planet.get_vel()))
        planet.update_position(Universe.TIME_STEP)
        pygame.draw.circle(screen, planet.get_color(), planet.get_pos(), planet.get_radius())
        pygame.draw.line(screen, (115, 115, 115), planet.get_pos(), vec_add(planet.get_pos(), vec_mul(planet.get_vel(), 30)))
        text = font_renderer.render(planet.name, True, (0, 0, 0))
        screen.blit(text, planet.get_pos())
    # flip the display
    pygame.display.flip()

pygame.quit()
