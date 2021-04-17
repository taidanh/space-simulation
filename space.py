#! /usr/bin/env python3
from Planet import *
import Universe

import numpy as np
import pygame
from pygame.locals import *

#           name           pos        vel       radius   color       surface_gravity
p1 = Planet("walnut",   (640, 360), (2, 0),       50, (0, 0, 255), 7000)
p2 = Planet("bruh",     (640, 450), (-400, 0),    15, (0, 255, 0), 10)
p3 = Planet("tucan",    (800, 200), (-200, -200), 30, (255, 0, 0), 200)
p4 = Planet("moon",     (800, 155), (-290, -160), 5,  (115, 115, 115), 50)

all_planets: [Planet] = [p1, p2, p3, p4]
radius: int = 20

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

# press SPACE to start simulation
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

    # black background
    screen.fill((0, 0, 0))

    # draw connecting lines between planets
    for i in range(len(all_planets)):
        for k in all_planets[i:]:
            pygame.draw.line(screen, (255, 255, 255), all_planets[i].get_pos(), k.get_pos())

    # do physics on all planets
    for planet in all_planets:
        planet.update_velocity(all_planets, Universe.TIME_STEP)
        # print("{}'s vel =\t[{:.3f}, {:.3f}],\tnormed = {}".format(
        #    planet.name, planet.v[0], planet.v[1], planet.get_vel()))
        planet.update_position(Universe.TIME_STEP)
        pygame.draw.circle(screen, planet.get_color(), planet.get_pos(), planet.get_radius())
        pygame.draw.line(screen, (115, 115, 115), planet.get_pos(), vec_add(planet.get_pos(), vec_mul(planet.get_vel(), 30)))
        text = font_renderer.render(planet.name, True, (255, 255, 255))
        screen.blit(text, planet.get_pos())
    
    # draw circle around cursor
    x_mouse, y_mouse = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (255, 255, 255), (x_mouse, y_mouse), radius, width=1)

    # flip the display
    pygame.display.flip()

pygame.quit()
