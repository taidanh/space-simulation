#! /usr/bin/env python3
import Universe

import numpy as np
import pygame

def vec_add(vec1, vec2):
    if (len(vec1) == len(vec2)):
        v = np.array([], dtype=float)
        for i in range(len(vec1)):
            v = np.append(v, vec1[i] + vec2[i])
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

class Planet():
    def __init__(self, x_vel: float, y_vel: float):
        self.pos = np.array([0, 0], dtype=int)        # x and y position
        self.x = np.array([0, 0], dtype=np.float)    # x and y position
        self.v = np.array([0., 0.], dtype=np.float)    # x and y velocity
        self.a_g = np.array([0., 0.], dtype=np.float)  # x and y acceleration
        self.t = 0.0            # current time
        self.dt = 0.0           # current time step
        self.a = 0      # semimajor axis of the orbit
        self.e = 0   # eccentricity of the orbit
        self.istep = 0          # current int timestep1
        self.name: str = ""
        self.color = np.array([255, 255, 255], dtype=int)
        self.radius: int = 0
        self.surface_gravity:float = 0.0

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

    def update_velocity(self, all_planets, time_step: float):
        for planet in all_planets:
            if planet != self:
                sqrt_dist: float = vec_sqt(vec_pow((planet.pos - self.pos), 2))
                force_dir = vec_sqt(vec_pow((planet.pos - self.pos), 2))
                # acceleration = vec_mul(force_dir, (Universe.GRAV_CONST * planet.get_mass() / sqrt_dist))
                acceleration = force_dir * Universe.GRAV_CONST * planet.get_mass() / sqrt_dist
                self.v += acceleration * time_step

    def update_position(self, time_step: float):
        self.pos = vec_add(self.pos, vec_mul(self.v, time_step))
