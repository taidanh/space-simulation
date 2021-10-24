#! /usr/bin/env python3
from Planet import *
import Universe
import ui

from random import randint
import numpy as np
import pygame
from pygame.locals import *

#           name           pos        vel       radius   color       surface_gravity
p1 = Planet("walnut",   (640, 360), (2, 0),       50, (0, 0, 255), 7000)
p2 = Planet("bruh",     (640, 450), (-400, 0),    15, (0, 255, 0), 10)
p3 = Planet("raq",    (800, 200), (-200, -200), 30, (255, 0, 0), 200)
p4 = Planet("moon",     (800, 155), (-290, -160), 5,  (115, 115, 115), 50)
p5 = Planet("luis",     (700, 255), (-290, -160), 5,  (115, 115, 115), 50)

all_planets: [Planet] = [p1, p2, p3, p4, p5]
radius: int = 20

def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


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

center = (90, window[1] - 170)
box_pos = (10, window[1] - 250)
angle = (center[0], center[1] - 70)
box = ui.draw_planet_picker(box_pos, center, (115,115,115), (75,75,75), screen)

multiplier: float = 0
last_event = 0

running = True
pause = True

while running:

    screen.fill((0, 0, 0))

    dt = clock.tick()
    
    last_event += dt


    # draw connecting lines between planets
    # ui.draw_planet_connecting_lines(all_planets, (255,255,255), screen)

    # do physics on all planets
    for planet in all_planets:
        if (not pause):
            planet.update_velocity(all_planets, Universe.TIME_STEP)
            planet.update_position(Universe.TIME_STEP)
        pygame.draw.circle(screen, planet.get_color(), planet.get_pos(), planet.get_radius())
        pygame.draw.line(screen, (115, 115, 115), planet.get_pos(), vec_add(planet.get_pos(), vec_mul(planet.get_vel(), 30)))
        text = font_renderer.render(planet.name, True, (255, 255, 255))
        screen.blit(text, planet.get_pos())
    
#    box = pygame.draw.rect(screen, (115, 115, 115), (10, window[1] - 260, 160, window[1] - 10))
#    pygame.draw.circle(screen, (75, 75, 75), box_pos, 70)
    angle = ui.planet_picker(box_pos, angle, (115,115,115), (75,75,75), screen)

    # draw circle around cursor
    if (box.collidepoint(pygame.mouse.get_pos()) == False):
        pygame.draw.circle(screen, (255, 255, 255), pygame.mouse.get_pos(), radius, width=1)
        if (pygame.mouse.get_pressed()[0] and last_event > 250):
            all_planets.append(Planet("unnamed", pygame.mouse.get_pos(), vec_mul(vec_nrm(vec_sub(angle, center)), randint(100, 400)), radius,  rand_color(), 15))
            last_event = 0


    # flip the display
    pygame.display.flip()


    # check if user closed game
    for event in pygame.event.get():
        if event.type == QUIT:
            print("quitting game...")
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_SPACE:
                pause ^= 1
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 4:
                radius += 2
            if event.button == 5:
                if (radius - 2) > 0:
                    radius -= 2


pygame.quit()
