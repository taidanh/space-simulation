#! /usr/bin/env python3
import Universe

import numpy as np
import pygame


def vec_sqrt(x):
    v = np.array(0, dtype=float)
    for i in x:
        np.append(v, np.sqrt(i))
    return v

def vec_mult(vec, scalar):
    v = np.array(0, dtype=float)
    for i in vec:
        np.append(v, i * scalar)
    return v

def vec_div(vec, scalar):
    v = np.array(0, dtype=float)
    for i in vec:
        np.append(v, i / scalar)
    return v


class Planet():
    def __init__(self, semimajor: float, eccentricity: float):
        self.x = np.array([0., 0.], dtype=np.float)    # x and y position
        self.v = np.array([0., 0.], dtype=np.float)    # x and y velocity
        self.a_g = np.array([0., 0.], dtype=np.float)  # x and y acceleration
        self.t = 0.0            # current time
        self.dt = 0.0           # current time step
        self.a = semimajor      # semimajor axis of the orbit
        self.e = eccentricity   # eccentricity of the orbit
        self.istep = 0          # current int timestep1
        self.name: str = ""
        self.color = np.array([255, 255, 255])
        self.radius: int = 0
        self.surface_gravity:float = 0.0

    def get_radius(self):
        return self.radius

    def set_pos(self, x, y):
        self.x[0], self.x[1] = x, y

    def get_pos(self):
        return self.x[0], self.x[1]

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
                sqrt_dist: float = vec_sqrt(planet.x - self.x)
                force_dir = vec_sqrt((planet.x - self.x) ** 2)
                acceleration = vec_div(vec_mult(vec_mult(force_dir, Universe.GRAV_CONST), planet.get_mass()), sqrt_dist)
                acceleration = force_dir * Universe.GRAV_CONST * planet.get_mass() / sqrt_dist
                self.v += acceleration * time_step

    def update_position(self, time_step: float):
        self.get_pos + self.v * time_step
