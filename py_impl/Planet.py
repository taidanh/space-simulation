#! /usr/bin/env python3
import Universe

import numpy as np
import pygame

#--------------------------#
# Vector, scalar functions #
#--------------------------#

def vec_add(vec1, vec2):
    if (len(vec1) == len(vec2)):
        v = np.array([], dtype=float)
        for i in range(len(vec1)):
            v = np.append(v, vec1[i] + vec2[i])
        return v

def vec_sub(vec1, vec2):
    if (len(vec1) == len(vec2)):
        v = np.array([], dtype=float)
        for i in range(len(vec1)):
            v = np.append(v, vec1[i] - vec2[i])
        return v

def vec_sqt(x):
    v = np.array([], dtype=float)
    for i in range(len(x)):
        v = np.append(v, np.sqrt(x[i]))
    return v

def vec_mul(vec, scalar):
    v = np.array([], dtype=float)
    for i in vec:
        v = np.append(v, i * scalar)
    return v

def vec_div(vec, scalar):
    v = np.array([], dtype=float)
    for i in range(len(vec)):
        v = np.append(v, vec[i] / scalar)
    return v

def vec_pow(vec, pow):
    v = np.array([], dtype=float)
    for i in range(len(vec)):
        v = np.append(v, vec[i] ** pow)
    return v

def vec_mag(vec):
    sum: float = 0
    for i in vec:
        sum += i ** 2
    return np.sqrt(sum)

def vec_dst(vec1, vec2):
    if (len(vec1) == len(vec2)):
        sum: float = 0
        for i in range(len(vec1)):
            sum += (vec1[i] - vec2[i]) ** 2
        return sum
    return -1

def vec_nrm(vec):
    return vec_div(vec, vec_mag(vec))


#--------------#
# Planet Class #
#--------------#

class Planet():
    def __init__(self, name: str, pos: [float], vel: [float], radius: int, color: [int], grav: float):
        self.pos: [float] = np.array(pos, dtype=float)          # x and y position
        self.v: [float] = np.array(vel, dtype=np.float)     # x and y velocity
        self.name: str = name
        self.color: [int] = np.array(color, dtype=int)
        self.radius: int = radius
        self.surface_gravity:float = grav

    def get_radius(self):
        return self.radius

    def set_pos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
        return

    def get_pos(self):
        x = self.pos[0]
        y = self.pos[1]
        return (x, y)

    def set_color(self, r: int, g: int, b: int):
        self.color[0] = r
        self.color[1] = g
        self.color[2] = b

    def get_color(self):
        return self.color[0], self.color[1], self.color[2]

    def get_mass(self):
        return self.surface_gravity * self.radius * self.radius / Universe.GRAV_CONST

    def get_vel(self):
        return vec_nrm(self.v)

    def update_velocity(self, all_planets, time_step: float):
        for planet in all_planets:
            if planet != self:
                dst_sqr: float = vec_dst(planet.pos, self.pos)
                force_dir: [float] = vec_nrm(vec_sub(planet.get_pos(), self.get_pos()))
                force: [float] = force_dir * Universe.GRAV_CONST * self.get_mass() * planet.get_mass() / dst_sqr
                acceleration: [float] = force / self.get_mass()
                self.v += vec_mul(acceleration, time_step)

    def update_position(self, time_step: float):
        self.pos = vec_add(self.pos, vec_mul(self.v, time_step))
