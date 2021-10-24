from Planet import *

import pygame
from pygame.locals import *

def point_to_circle(radius: float, c: (float), p: (float)):
    cx, cy = c
    px, py = p
    vx: float = px - cx
    vy: float = py - cy
    magV: float = vec_mag((vx, vy))
    ax: float = cx + vx / magV * radius
    ay: float = cy + vy / magV * radius
    return (ax, ay)

def point_to_angle(radius: float, center: (float), point: (float)):
    pass

def draw_planet_picker(pos, center, color_rect, color_circle, screen):

    # draw box and circle for UI
    box = pygame.draw.rect(screen, color_rect, 
            (pos[0],
                pos[1],
                pos[0] + 150, 
                pos[1] + 180))
    pygame.draw.circle(screen, color_circle, center, 70)
    return box

def planet_picker(pos, angle, color_rect, color_circle, screen):  # -> pygame rect
    center = (pos[0] + 80, pos[1] + 80)

    box = draw_planet_picker(pos, center, color_rect, color_circle, screen)

    # calculate angle of picker inside circle
    if (box.collidepoint(pygame.mouse.get_pos())):
        if (pygame.mouse.get_pressed()[0]):
            x, y = pygame.mouse.get_pos()
            angle = point_to_circle(70, center, (x, y))

    # draw angle of picker
    pygame.draw.line(screen, (255, 255, 255), center, angle)
    return angle

def draw_planet_connecting_lines(all_planets, color, screen):
   for i in range(len(all_planets)):
       for k in all_planets[i:]:
           pygame.draw.line(screen, color, all_planets[i].get_pos(), k.get_pos())
